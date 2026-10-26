# Akshay Kumar — Portfolio

## Optional Telegram visitor alerts — 26 October 2026

The two public portfolio pages load `assets/visitor-alerts.js` without any popup or floating controls. Alerts are disabled until a valid private server configuration is installed. Visitors must opt in before a notification is sent; the footer’s Privacy & analytics link opens a separate page for opt-in and withdrawal. DNT/GPC and owner exclusion are respected. This feature is a visit notification service, not an identity lookup or an online visitor dashboard.

The PHP endpoint at `api/visitor-alert.php` reads `domains/theakshaydev.space/private-visitor-alerts/telegram.json`, outside `public_html`. Keep that directory at mode 700 and the file at mode 600. JSON fields: `enabled` (boolean), `bot_token` (secret string), `chat_id` (private destination ID string). Never put the configuration into this repository, a public upload folder or a ZIP. PHP 8.1+ with cURL is required; no database or always-running worker is needed.

Messages contain page, India time, device/OS categories and referring hostname. No raw IP, URL queries, contact details or geolocation are sent. Rate-limit state stores only keyed hashes. Limits: one notification per browser-tab session while its server hash remains within 30 minutes, one per connection IP per minute, 20 globally per minute. Duplicates and malformed/off-origin requests are rejected. A delivery failure is logged without response contents or secrets; the reservation remains to avoid retry storms.

Owner exclusion: open `https://theakshaydev.space/?visitor_alerts=off` in each browser you use. Use `?visitor_alerts=on` to undo that exclusion. Both preferences are stored only in that browser. Privacy information is at `/privacy.html`.

Validate PHP with `php -l api/visitor-alert.php`, JavaScript with `node --check assets/visitor-alerts.js`, and check consent/rejection/duplicates/rate limits before activation. Test messages must go only to the owner's verified chat. Rotating a bot token also invalidates previous server hash keys. The public GET status exposes only `enabled`, never configuration or visitor data.

## SEO update — 25 October 2026

- Updated portfolio metadata for freelance web development and network engineering in New Delhi, while retaining the existing research and cybersecurity content.
- Added a visible services section and `web-development.html` with real project references, enquiry links and project-scope FAQs.
- Added Person/ProfilePage and Service/Breadcrumb structured data, canonical URLs, `robots.txt` and a two-page `sitemap.xml`.
- Search Console ownership uses the HTML verification tag; website DNS records are not changed.
- The hosting ZIP now includes `index.html`, `web-development.html`, `robots.txt`, `sitemap.xml` and `assets/` at its root.


Personal portfolio of Akshay Kumar, System & Network Engineer, Researcher and aspiring penetration tester. Built with HTML, CSS and JavaScript.


**Live website:** [View portfolio](https://theakshaydev.space/)


## Latest portfolio package


[Download the updated portfolio ZIP](akshay-portfolio-updated-hosting.zip)


This deployable package is generated from the current index.html and assets/ source. Upload it to Hostinger to publish these changes; changing this repository alone does not confirm a live deployment.


## Open or deploy


1. Download and extract `akshay-portfolio-updated-hosting.zip`.
2. Open `index.html` to preview the portfolio locally. Keep the `assets` folder beside it.
3. Upload the extracted public files, including `api/` and `assets/`, into the domain public_html folder on Hostinger. No build command, Node.js or database is required. The optional notification endpoint needs PHP; credentials are configured separately outside the public folder.


## Profiles


- [GitHub](https://github.com/akshay7549)
- [LinkedIn](https://www.linkedin.com/in/akshay-kumar-090990249/)


## Research


[Google Scholar - publication profile](https://scholar.google.com/citations?user=n_KkLYUAAAAJ&hl=en)


The live portfolio highlights selected publications where Akshay Kumar is first author: Intrusion Detection Systems and Cloud Communications and Networks. Author order was verified against the publisher pages.



## Original reference archive

[Original reference ZIP](akshay-portfolio-profile-reference.zip) is preserved alongside the current source and deployment package.

## Current improvements

Mobile navigation, prominent name and role, local resume download, twelve project details, keyboard-accessible blog dialogs, real project previews and publisher/DOI links.

### Projects update — 24 October 2026

- Added NextGen Lapy World with repair booking, tracking and device catalogue details verified from https://nextgenlapyworld.in/.
- Added Khushi Decoration & Seasonal Store, Python Inventory Management and Python ATM Interface from the public repositories under https://github.com/akshay7549.
- Added repository links to the existing CCTV and Kasvi Place project dialogs. Existing project content and the deployed Sukoon stack remain unchanged.
- Checked JavaScript syntax, twelve unique project detail IDs, sibling card structure, local assets and HTTPS link formatting. Browser preview confirmed the new cards, NextGen dialog activation, Escape dismissal and focus return.

The hosting ZIP includes these updates. GitHub source publication does not deploy the Hostinger website; upload the ZIP contents to the domain's `public_html` directory to publish.

### Mobile layout and reading-time fixes

- At widths up to 700px, the introduction and four action buttons appear before the portrait and service grid. Cards use normal grid flow instead of overlapping absolute positions.
- Home, section and Journey anchors account for the sticky header. Decorative elements do not create horizontal overflow.
- Contact labels and values use separate stacked rows, including wrapping for long email addresses. Mobile action buttons have a minimum 44px height.
- All five field-note cards and their dialogs calculate reading time from the actual article body at 200 words per minute, rounded up with a one-minute minimum. Existing short notes correctly show 1 MIN READ. Article text is unchanged.
- Journey is inside the main landmark, before Contact and the footer.
- Canonical URL, Open Graph and Twitter metadata reference the production domain and existing portrait asset.
- Project dialogs link to the relevant repositories. Research links distinguish direct posts from general LinkedIn profile references; exact ICETCE and ISBM post URLs still need to be supplied.

Validation: browser checks at 320x740, 390x844, 768x1024 and 1440x900; zero horizontal overflow at those sizes, mobile menu and Home/Contact navigation, article dialog reading-time labels, focus containment, Escape dismissal and focus return. JavaScript syntax and local asset/anchor checks also pass.

To rebuild the upload ZIP with PowerShell, run `Compress-Archive -Path index.html, assets -DestinationPath akshay-portfolio-updated-hosting.zip -Force`. The ZIP root must contain index.html and assets/, including assets/qa-fixes.css.
