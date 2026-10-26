<?php
declare(strict_types=1);
// Credentials and rate-limit state live outside public_html, never in Git.
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
header('X-Content-Type-Options: nosniff');
function respond(int $status, array $body): never {
    http_response_code($status);
    echo json_encode($body);
    exit;
}
$private = dirname(__DIR__, 2) . '/private-visitor-alerts';
$configFile = $private . '/telegram.json';
$config = is_readable($configFile) ? json_decode((string) file_get_contents($configFile), true) : [];
$ready = is_array($config) && ($config['enabled'] ?? false) === true
    && preg_match('/^\d{6,}:[A-Za-z0-9_-]{20,}$/D', (string) ($config['bot_token'] ?? ''))
    && preg_match('/^-?\d+$/D', (string) ($config['chat_id'] ?? ''));
if ($_SERVER['REQUEST_METHOD'] === 'GET') respond(200, ['enabled' => (bool) $ready]);
if ($_SERVER['REQUEST_METHOD'] !== 'POST') respond(405, ['ok' => false]);
if (!$ready) respond(503, ['ok' => false, 'reason' => 'inactive']);
// Exact origin and fixed event fields: no arbitrary messages or recipients.
if (($_SERVER['HTTP_ORIGIN'] ?? '') !== 'https://theakshaydev.space') respond(403, ['ok' => false]);
if (!str_starts_with(strtolower($_SERVER['CONTENT_TYPE'] ?? ''), 'application/json')
    || (int) ($_SERVER['CONTENT_LENGTH'] ?? 0) > 2048) respond(400, ['ok' => false]);
$input = json_decode((string) file_get_contents('php://input', false, null, 0, 2049), true);
if (!is_array($input) || ($input['consent'] ?? false) !== true
    || !preg_match('/^[a-f0-9-]{32,36}$/D', (string) ($input['session'] ?? ''))
    || !in_array($input['page'] ?? '', ['/', '/index.html', '/web-development.html'], true)) respond(400, ['ok' => false]);
if (!function_exists('curl_init')) respond(503, ['ok' => false]);
$ip = $_SERVER['REMOTE_ADDR'] ?? '';
// Only trust the CDN IP header when the immediate peer is Cloudflare.
// No client-supplied X-Forwarded-For header is trusted here.
function inNetwork(string $ip, string $cidr): bool {
    [$network, $bits] = explode('/', $cidr);
    $address = @inet_pton($ip); $base = @inet_pton($network);
    if ($address === false || $base === false || strlen($address) !== strlen($base)) return false;
    $bytes = intdiv((int) $bits, 8); $remainder = (int) $bits % 8;
    return substr($address, 0, $bytes) === substr($base, 0, $bytes)
        && (!$remainder || ((ord($address[$bytes]) ^ ord($base[$bytes])) & (0xff << (8 - $remainder))) === 0);
}
$cloudflare = ['173.245.48.0/20','103.21.244.0/22','103.22.200.0/22','103.31.4.0/22','141.101.64.0/18','108.162.192.0/18','190.93.240.0/20','188.114.96.0/20','197.234.240.0/22','198.41.128.0/17','162.158.0.0/15','104.16.0.0/13','104.24.0.0/14','172.64.0.0/13','131.0.72.0/22','2400:cb00::/32','2606:4700::/32','2803:f800::/32','2405:b500::/32','2405:8100::/32','2a06:98c0::/29','2c0f:f248::/32'];
foreach ($cloudflare as $range) {
    if (inNetwork($ip, $range)) {
        $candidate = $_SERVER['HTTP_CF_CONNECTING_IP'] ?? '';
        if (filter_var($candidate, FILTER_VALIDATE_IP)) $ip = $candidate;
        break;
    }
}
$now = time();
$salt = (string) $config['bot_token'];
$ipKey = hash_hmac('sha256', $ip, $salt);
$sessionKey = hash_hmac('sha256', $ip . '|' . $input['session'], $salt);
$lock = @fopen($private . '/rate-limits.json', 'c+');
if (!$lock || !flock($lock, LOCK_EX)) respond(503, ['ok' => false]);
$state = json_decode(stream_get_contents($lock), true) ?: [];
foreach (['sessions' => 1800, 'ips' => 60] as $bucket => $ttl) {
    $state[$bucket] = array_filter($state[$bucket] ?? [], fn($time) => is_int($time) && $time > $now - $ttl);
}
$state['sent'] = array_values(array_filter($state['sent'] ?? [], fn($time) => is_int($time) && $time > $now - 60));
if (isset($state['sessions'][$sessionKey])) { flock($lock, LOCK_UN); fclose($lock); respond(200, ['ok' => true, 'duplicate' => true]); }
if (isset($state['ips'][$ipKey]) || count($state['sent']) >= 20) { flock($lock, LOCK_UN); fclose($lock); respond(429, ['ok' => false]); }
// Reserve before sending, so concurrent requests cannot produce duplicate alerts.
$state['sessions'][$sessionKey] = $now;
$state['ips'][$ipKey] = $now;
$state['sent'][] = $now;
rewind($lock); ftruncate($lock, 0); fwrite($lock, json_encode($state)); fflush($lock);
flock($lock, LOCK_UN); fclose($lock); @chmod($private . '/rate-limits.json', 0600);
function clean(string $value, int $length): string {
    return substr(preg_replace('/[\x00-\x1F\x7F]/', '', $value) ?? '', 0, $length);
}
$device = in_array($input['device'] ?? '', ['Mobile', 'Tablet', 'Desktop'], true) ? $input['device'] : 'Unknown';
$platform = in_array($input['platform'] ?? '', ['Android', 'iOS', 'Windows', 'macOS', 'Linux', 'Other'], true) ? $input['platform'] : 'Other';
$source = 'Direct / unavailable';
if (is_string($input['source'] ?? null)) {
    $host = parse_url($input['source'], PHP_URL_HOST);
    if (is_string($host) && preg_match('/^[a-zA-Z0-9.-]{1,160}$/D', $host)) $source = $host;
}
$message = "New portfolio visitor\nWebsite: theakshaydev.space\nTime: " . (new DateTimeImmutable('now', new DateTimeZone('Asia/Kolkata')))->format('d M Y, h:i A')
    . " IST\nPage: " . $input['page'] . "\nDevice: " . $device . ' / ' . $platform
    . "\nSource: " . clean($source, 160) . "\nVisitor consent: granted\nIdentity and exact location: unavailable";
$curl = curl_init('https://api.telegram.org/bot' . $config['bot_token'] . '/sendMessage');
curl_setopt_array($curl, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => http_build_query([
    'chat_id' => (string) $config['chat_id'], 'text' => $message, 'disable_web_page_preview' => 'true'
]), CURLOPT_RETURNTRANSFER => true, CURLOPT_CONNECTTIMEOUT => 3, CURLOPT_TIMEOUT => 6,
CURLOPT_PROTOCOLS => CURLPROTO_HTTPS]);
$result = curl_exec($curl);
$status = curl_getinfo($curl, CURLINFO_RESPONSE_CODE);
curl_close($curl);
$reply = is_string($result) ? json_decode($result, true) : null;
if ($status !== 200 || !is_array($reply) || ($reply['ok'] ?? false) !== true) {
    // No tokens, IP addresses or Telegram response contents go into the public response or log.
    error_log('Portfolio visitor alert delivery failed. HTTP ' . $status);
    respond(502, ['ok' => false]);
}
respond(200, ['ok' => true]);
