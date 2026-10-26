(() => {
  'use strict';
  const endpoint = '/api/visitor-alert.php';
  const key = 'portfolio-visitor-consent-v1';
  const ownerKey = 'portfolio-owner-exclude-v1';
  const read = (store, name) => { try { return store.getItem(name); } catch { return null; } };
  const save = (store, name, value) => { try { store.setItem(name, value); } catch {} };
  const owner = new URLSearchParams(location.search).get('visitor_alerts');
  if (owner === 'off') save(localStorage, ownerKey, 'yes');
  if (owner === 'on') save(localStorage, ownerKey, 'no');
  const excluded = () => read(localStorage, ownerKey) === 'yes'
    || navigator.doNotTrack === '1' || navigator.globalPrivacyControl === true;
  const send = async () => {
    if (excluded() || read(localStorage, key) !== 'yes' || document.visibilityState !== 'visible') return;
    if (read(sessionStorage, 'portfolio-visit-sent-v1') === 'yes') return;
    let session = read(sessionStorage, 'portfolio-visit-session-v1');
    if (!session) { session = crypto.randomUUID(); save(sessionStorage, 'portfolio-visit-session-v1', session); }
    const ua = navigator.userAgent;
    const device = /iPad|Tablet/i.test(ua) ? 'Tablet' : /Mobile|Android|iPhone/i.test(ua) ? 'Mobile' : 'Desktop';
    const platform = /Android/i.test(ua) ? 'Android' : /iPhone|iPad|iPod/i.test(ua) ? 'iOS' : /Windows/i.test(ua) ? 'Windows' : /Mac/i.test(ua) ? 'macOS' : /Linux/i.test(ua) ? 'Linux' : 'Other';
    let source = '';
    try { if (document.referrer) { const ref = new URL(document.referrer); if (ref.origin !== location.origin) source = ref.origin; } } catch {}
    try {
      const response = await fetch(endpoint, { method: 'POST', credentials: 'omit', keepalive: true,
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ consent: true, session, page: location.pathname, device, platform, source }) });
      if (response.ok || response.status === 429) save(sessionStorage, 'portfolio-visit-sent-v1', 'yes');
    } catch { /* Analytics never interrupts the portfolio. */ }
  };
  // Preferences are available on the privacy page through the footer.
  // Never display an automatic prompt or a floating control.
  if (excluded() || read(localStorage, key) !== 'yes') return;
  fetch(endpoint, { credentials: 'omit', cache: 'no-store' }).then(r => r.ok ? r.json() : { enabled: false }).then(config => {
    if (!config.enabled) return;
    void send();
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') void send(); });
  }).catch(() => {});
})();
