# Akshay Kumar — Portfolio


Personal portfolio of Akshay Kumar, System & Network Engineer, Researcher and aspiring penetration tester. Built with HTML, CSS and JavaScript.


**Live website:** [View portfolio](https://theakshaydev.space/)


## Latest portfolio package


[Download the updated portfolio ZIP](akshay-portfolio-updated-hosting.zip)


This deployable package is generated from the current index.html and assets/ source. Upload it to Hostinger to publish these changes; changing this repository alone does not confirm a live deployment.


## Open or deploy


1. Download and extract `akshay-portfolio-updated-hosting.zip`.
2. Open `index.html` to preview the portfolio locally. Keep the `assets` folder beside it.
3. Upload the extracted index.html and assets/ folder into the domain public_html folder on Hostinger. No build command, Node.js or database is required.


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
