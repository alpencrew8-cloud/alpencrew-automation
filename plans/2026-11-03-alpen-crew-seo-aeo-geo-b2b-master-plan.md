# ALPEN CREW — INTERNATIONAL B2B WEBSITE & ORGANIC GROWTH MASTER PLAN
**Version:** 1.0 | **Evidence cutoff:** 3 November 2026 | **Owner:** alpencrew8-cloud | **Execution operator:** authorized GitHub collaborator from the user's ChatGPT account | **Budget:** free tools only

> **Plan status:** Evidence-based plan completed. Existing public SEO scans and WordPress authenticated *read tests* succeeded. No production SEO/content/theme/social settings have been modified under this plan. All live changes require the P0 safety gate below. This file is the source-of-truth roadmap and should be updated with commit IDs, before/after evidence and owner approvals as work advances.

## 1. Executive decision

**Commercial objective:** Turn Alpen Crew's existing WordPress/WooCommerce website from a mixed manufacturer/shop/demo-theme site into a credible, searchable, easy-to-contact Bavarian/Trachten **B2B supplier** website that generates qualified RFQs, business buyer conversations and repeat opportunities.

**Recommended sequence:** Secure and restore-capable production setup → repair title/description/OG/canonical templates → remove or correctly handle demo pages → improve the business positioning, product and category content → build verifiable manufacturer evidence and RFQ process → optimize mobile, images and Core Web Vitals → localize real German commercial content → build reliable measurement, Instagram display and editorial/AI discoverability.

**What success means:** Not just better SEO health scores. A buyer must be able to find relevant real apparel products, understand Alpen Crew's verified manufacturing capabilities, submit specifications and quantities, receive a reliable response, and progress from enquiry to qualified quote/sample/order.

### 1.1 Verified baseline (no estimated traffic or rankings)

Source: [211-URL public SEO audit](../reports/2026-11-03-full-211-url-seo-frontend-audit.md) and [original Actions run](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664612642).

| Metric, 3 Nov 2026 | Observed |
|---|---:|
| URLs in public XML sitemap | 211 |
| Product URLs | 140 |
| Product-category URLs | 22 |
| Blog/archive URLs | 13 |
| Other public pages/URLs | 36 |
| Missing meta description elements | 211 / 211 |
| Missing OG title elements | 211 / 211 |
| URLs involved in duplicate title groups | 118 |
| URLs without canonical link elements | 44 |
| URLs without H1 | 28 |
| URLs without detected JSON-LD | 6 |
| Pages with meta noindex | 3 — cart, checkout, my-account (appropriate) |

Source: [Browser audit](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41665480937).

| Homepage desktop/mobile check | Finding |
|---|---|
| HTTP status | 200 on both |
| H1 | Not found |
| Meta description | Not found |
| Visible broken images | 0 |
| Images missing/empty alt | 25 out of 27; decorative alt may legitimately be blank |
| Horizontal overflow | Not detected |
| JS page errors in short smoke test | 0 |
| Instagram links / Facebook links | 1 / 1 |
| WhatsApp links | 0 |
| Instagram feed markup | Not detected |

Source: [WordPress capability audit](../reports/2026-11-03-wordpress-capabilities.md): authenticated read-only WordPress posts/pages/media/types, WooCommerce products and plugins endpoints returned HTTP 200. WooCommerce, Elementor, Smash Balloon Instagram Feed, LiteSpeed Cache and JetBackup detected. Major SEO plugin families not detected under standard slugs. No successful production write is yet proven.

**Unknown until separately connected:** Google Search Console coverage and actual Google-selected canonicals, search impressions/clicks, ranking positions, organic sessions, indexed page totals, Core Web Vitals field data, business enquiries, form delivery, Instagram authentication state, backups that can actually be restored, keyword volumes, backlinks and commercial conversion rate.

## 2. Buyer and brand strategy

### 2.1 Target the buyers, not retail browsing

**Primary ideal customer profiles:** existing Trachten/Bavarian clothing brands; apparel importers, wholesalers and distributors; private-label buyers; purchasing managers at established traditional-wear retailers with repeat bulk orders; specialist sourcing firms.

**Secondary ICPs, after screening:** established eventwear suppliers, festival merchandise distributors, uniform/wardrobe companies and larger institutional buyers that actually buy in volume.

**Lead qualification:** business name and verifiable website, market/country, company role, product type, target quantity by style/color/size, expected timeline, customization requirements and decision process. Keep individual consumer requests outside the qualified-B2B score.

**Priority geography hypothesis:** Germany, Austria and Switzerland for Trachten buying intent; English-speaking international distributors as a second lane. This is a *strategy hypothesis*, not a ranking/traffic finding. Confirm real buying regions with the owner and GA4/GSC enquiry evidence.

**Unverified claims that MUST NOT be published before owner documents them:** in-house factory ownership, employee count, annual capacity, exact MOQ, sample lead times, bulk turnaround, certifications, test reports, REACH/other compliance, material origin, shipping times, rates, years in business, client logos, export destinations, guarantees and private-label service specifics.

### 2.2 Positioning and message architecture

**Proposed strategic positioning (conditional on actual capabilities):** Alpen Crew — B2B Bavarian & Trachten Apparel Manufacturing and Supply.

**Hero copy candidate, to owner-verify:** "Bavarian & Trachten Apparel for Brands and Wholesale Buyers." Supporting: "Explore Lederhosen, Dirndl and traditional-wear styles. Discuss custom specifications, quantities and sourcing requirements with our team."

**Primary CTA:** Request a Bulk Quote. **Secondary CTA:** Discuss a Custom Development / View Product Categories. Strong contact actions should be usable on mobile with a clear, honest response policy.

**Brand personality:** craftsmanship, heritage-inspired product expertise, manufacturing clarity and contemporary international procurement professionalism. Avoid stock Oktoberfest caricatures, exaggerated luxury claims or borrowed certifications.

**Proposed visual system for owner review:** deep forest green / warm ivory / walnut brown / restrained brass accents; a high-contrast readable font pair; consistent product cropping and real approved workshop/fabric imagery. This is a *design direction*, not a claimed existing brand identity.

**Brand trust evidence:** authentic team/facility photos where authorized, a short business history, verified location in Pakistan, legal business identity as approved, owned product photos, genuine material and finishing closeups, a documented production/QC workflow, and buyer process commitments only if operationally true.

## 3. Information architecture and B2B buyer journeys

Keep the site's valuable existing URLs stable where possible; first map current slugs, backlinks, internal links and product relationships.

**Proposed top navigation:**
Home | Products (Men, Women, Children, Accessories) | Manufacturing & Customization | How We Work | Quality & Materials | About Alpen Crew | Insights | Request Bulk Quote

**Recommended core URLs / sections (exact slugs and existing ownership to be audited first):**
- Home (brand intent, differentiator, top product lines, process, contact)
- Product category hub and real product categories (retaining valid URLs)
- Verified OEM/ODM/private-label capability page, only if owner confirms services
- Bulk ordering process / specification submission
- Sampling, customization and production process (owner-verified details only)
- Materials, sizes, fabrics, QC and packaging guide (only documented options)
- About / factory story / quality evidence
- B2B FAQ (practical procurement answers, not arbitrary FAQ schema)
- Contact / Request Bulk Quote with form success and mobile CTA
- Privacy and cookie/terms policy as applicable, drafted for legal review
- Original knowledge hub: product fit, sourcing guides, material care and buyer checklists

**Existing merchandise:** 140 product URL entries and 22 category URLs. Review children/men/women, Lederhosen short/Kniebund/long, Dirndl dresses/blouses, shirts, socks/shoes/accessories only where actual stock/catalog supports them.

**Sample buyer journey:** Google search for wholesale Lederhosen → relevant category page → genuine product examples and material/spec choices → Request Bulk Quote → form captures company and specification → email/CRM confirmation → qualification → meeting/quote → sample approval → purchase order. Instrument every major transition.

**Do not create:** hundreds of near-identical country doorway pages, non-existent local offices, empty category pages, fake shopping offers or copied competitor text.

## 4. Technical SEO remediation — fix template causes first

### P0: site safety, measurement and indexing truth
1. Test a restorable off-site backup (database, uploads, theme/customizations/plugins/settings) in an isolated environment; log restore verification. JetBackup being installed does **not** prove a usable backup exists.
2. Replace current admin Application Password with dedicated least-privilege automation credentials where compatible with needed endpoints. Review and restrict public GitHub collaborators, workflow write access, environment secrets, branch rules and approval gates.
3. Confirm domain ownership, HTTPS canonical domain, redirects, robots.txt, sitemap indices and actual GSC property. Compare crawl output with Google index coverage and chosen canonicals. Do not claim 211 pages are indexed merely because they are in the sitemap.
4. Capture before snapshots for every page edited; test production publishing only on an owner-approved low-risk pilot with rollback.

### P1: SEO metadata system
**211 missing descriptions and 211 missing OG titles** suggest sitewide configuration/template absence rather than 422 unrelated authoring problems. Audit theme SEO fields, hooks and conflicting plugins. Evaluate one current **free** SEO plugin (such as a supported Yoast/Rank Math free implementation) or equivalent compatible code, **not two** overlapping SEO plugins. Installation only after backup and conflict testing.

Create correct templates for homepage, product, category, blog/archives and pages. Test the HTML head on at least one page per template:
- exactly one meaningful, page-specific document title
- useful unique meta description reflecting the actual visible content
- correct og:title, og:description, og:image and social image aspect
- canonical self-reference for truly indexable unique pages
- correct robots controls, page title and corresponding H1
- no duplicate SEO/head tags from theme and plugin

**Important:** Google may choose its own snippets; meta descriptions are not guaranteed to be shown, nor are they a direct substitute for useful body content. No fixed Google meta-description character limit: write for accurate snippets and test rendering, not rigid keyword stuffing.

### P1: duplicate titles (118 affected URLs)
Group by parent style, SKU, variant, photo and target intent. Distinguish genuine variants from accidentally duplicated products and identical category titles:
- Real separate models: add truthful differentiating material, color, length, gender or model code where documented.
- Simple size/color variants: decide whether one parent WooCommerce variable product is preferable based on content and navigation. Use ProductGroup schema where legitimately supported.
- Exact duplicates with no standalone buyer value: consider consolidation and a relevant 301 after link/backlink analysis.
- **Never** auto-delete variants based only on slugs like "-2" or "-3".

### P1: canonicals, headings and indexability
- Audit **44 URLs with missing canonical elements**, especially categories/archives.
- Audit **28 URLs missing H1**; use an accurate natural H1 for real landing pages. One main H1 per page is a clean editorial default, not a guaranteed Google ranking rule.
- Preserve noindex on /cart/, /checkout/, /my-account/ unless formally justified.
- Remove utility, demo, search/filter and unwanted thin URLs from target XML sitemaps as appropriate.
- Confirm HTTP 200, 3xx, 404 and 410, hreflang only for real alternate language URLs, canonical/noindex/robots consistency, breadcrumbs and internal link paths.
- 301 redirects only to the genuinely closest relevant surviving content; otherwise appropriate 404/410, not blanket redirects to homepage.
- Validate Product markup on products, Organization on homepage, BreadcrumbList on real trails, Article on suitable editorial pieces and WebSite where meaningful. Do not add duplicate schema blindly.
- For a B2B RFQ item without an actual consumer price/order checkout, evaluate Product **snippet** rules rather than inventing MerchantListing offers, availability, stars, reviews or price.
- Open Graph and social preview image dimensions and crop should be tested in preview tools.

### P1: demo theme cleanup
Create a classified inventory for WoodMart furniture posts, portfolio, sample page, design-trend categories and other non-Trachten pages. For each item capture:
- URL, content owner, current navigation/internal links, backlinks, GSC search traffic, intent and target replacement.
- Action: keep & improve / merge / noindex / redirect / delete.
- Remove from menus, footer, recommendation widgets and internal product links after target is validated.
- Publish a redirect map with expected status; run broken-link crawl after cleanup.
- Deletion and irreversible changes require owner sign-off and verified backup.

### P2: on-page image SEO and Core Web Vitals
- Set meaningful product image alt describing what is visually present; allow blank alt for genuinely decorative visuals. Do not fabricate materials/colors from filenames.
- Standardize real product file names, image crop, responsive srcset, WebP/AVIF when supported, dimensions, compression and lazy loading below the fold. Prioritize hero/LCP image; never lazy-load the hero indiscriminately.
- Use real user data to target Google good CWV thresholds: **LCP <= 2.5s, INP <= 200ms, CLS <= 0.1 at p75**. Lab Lighthouse/PageSpeed tests support debugging, not field-data claims.
- Inspect heavy Elementor widgets, font loading, render-blocking CSS/JS, uncached templates, unused feed scripts and WooCommerce assets.
- Confirm LiteSpeed Cache works with the actual hosting stack before enabling more cache features. Test cart, quote forms, forms' CSRF tokens and login sessions against caching; avoid breaking WooCommerce checkout.
- Test mobile nav, typography, contrast, focus indicators, keyboard navigation and form error messages.

## 5. AEO and GEO — useful answers and verifiable citations

**Definitions for this plan:** AEO = answer engine optimization, GEO = generative engine optimization, *not* an excuse to promise placements in ChatGPT/Gemini/AI Overviews. International/geographic SEO is a separate workstream below.

Google's May 2026 guidance says established SEO, accessible indexed content and unique first-hand expertise form the basis of its generative search features; no special llms.txt file or AI-only schema is required for Google.

**Content architecture for being cited responsibly:**
- One clear, factual summary per core page, with precise natural terminology.
- Real product detail tables: garment type, fit, size chart, approved material/composition, finishing, relevant customization choices, care notes and packaging, without invented numbers.
- Procurement help pages addressing practical questions: "What information is needed to request a Lederhosen bulk quote?", "Which size breakdown should a distributor provide?", "How are sample and production approvals handled?", "What affects custom embroidery options?", "How should buyers specify Dirndl colors and fabrics?".
- Explain honest supply boundaries, samples, order steps, quality checks and inspection documentation **only with owner-verified procedures**.
- Publish original factory/production photographs and expert-reviewed sourcing explanations to create evidence AI summaries and B2B buyers cannot get from generic replicated articles.
- Add internal links from Q&A content to product categories and RFQ. Keep technical information in crawlable HTML, not images alone.
- Create topical coverage with perhaps **8–12 carefully researched, original anchor guides** over 90 days rather than hundreds of AI-generated thin posts. Proposed number is a capacity plan, not a Google requirement.
- Keep FAQ as useful visible content; do **not** forecast FAQ rich-result snippets for a commercial clothing website (Google limits them substantially).
- Build brand entity consistency with verified official company name, logo, website, public social links, phone/email and address where approved. Add matching Organization schema; no fake third-party citations.
- Do not automatically block legitimate search crawlers, but preserve normal security and privacy. Do not expose private quote/lead records to crawlers.
- Evaluate Google Search Console appearance, organic search and referral logs. For AI answer visibility, manually sample a consistent monthly basket of buyer queries and record exact response/source links, locations, dates and model/platform; do not invent API-based "share of AI voice".

**Search/AI question clusters:** manufacturer vs wholesaler, leather vs suede specifications, garment customizations, B2B quantities and size runs, Trachten fit, packaging/QC expectations, sourcing from Pakistan, import documentation (fact-checked, not legal advice), wholesale collection planning, Dirndl and Lederhosen sourcing workflows.

## 6. B2B keyword and page strategy (keyword ideas, not measured volumes)

Real keyword targets require free GSC and Bing query data, competition review and buyer-qualified search intent. This proposed map is a research queue, **not** proof of current rankings or demand:

| Priority | Buyer-intent query cluster | Target page / action |
|---|---|---|
| P1 | wholesale Lederhosen; Lederhosen supplier | Existing relevant Lederhosen category, rewrite |
| P1 | Lederhosen manufacturer; bulk Lederhosen | Verified manufacturing capability / category hub |
| P1 | private-label Lederhosen; custom Lederhosen manufacturer | Custom/private-label page only if true |
| P1 | Dirndl dress wholesale; Dirndl supplier | Existing Dirndl category, rewrite |
| P1 | private label Dirndl dresses | Existing product collection + verified service page |
| P1 | Trachten shirts wholesale; traditional Bavarian shirts supplier | Existing Trachten shirts category |
| P1 | Trachten clothing manufacturer; Bavarian clothing supplier | Homepage and manufacturing capabilities |
| P1 | Kinder Lederhosen wholesale; boys Lederhosen supplier | Children/Boys category |
| P2 | women Lederhosen supplier | Women category |
| P2 | Trachten blouses wholesale | Existing blouse category |
| P2 | Kniebundhosen manufacturer; long Lederhosen | Relevant existing styles |
| P2 | Trachten socks and accessories wholesale | Genuine accessories category |
| P2 | OEM Trachten clothing / custom embroidery on traditional wear | Services only after verifying actual offering |
| P2 | German-language wholesale Trachten terms | Real German translated/localized categories |
| P2 | traditional clothing sourcing QC, sizing and development | Original educational guides |

**On-page SEO rule:** One primary intent per important URL, with supporting related phrases naturally integrated. Do not repeat 30 variants of the same phrase across cloned pages. Improve buyer decision-making, not word count.

### Recommended content templates

**Homepage:** identity → product categories → verified manufacturing/services → why work with us (evidence) → how ordering works → proof gallery → top FAQs → contact/quote.

**Category:** natural H1 → 150–300 words *if genuinely useful*, category filter/gallery → validated materials and business buying options → 3–5 real FAQ answers → related collections → quote CTA. The length is illustrative, not an SEO ranking threshold.

**Product:** accurate unique title and SKU → gallery → model features → fit/size chart → actual fabric/material data → verified branding/customization options → packaging/sample process → bulk quote CTA → breadcrumb/related variants. Validate Product schema, no fake prices or ratings.

**Original article:** buyer problem → first-hand explanation → verified technical examples and photos → sourcing checklist → evidence/citations → relevant product/RFQ links → named/approved editorial reviewer.

**Meta description example (illustrative, do not publish until services confirmed):** "Explore [verified item] options for business sourcing. Share your specification, quantities and branding requirements with Alpen Crew to request a bulk quotation." Product-specific words must replace placeholders.

## 7. International and language SEO

Prioritize where buyer evidence and language quality support the work:
1. Keep a reliable English master site and its actual canonical URLs.
2. Owner-approve carefully edited **German** product/category/service pages if German-speaking buyer segment is real. Publish only complete native-quality main content; no mixed English/German or auto-generated keyword pages.
3. Use true localized URLs with reciprocal hreflang (de/de-DE, de-AT, de-CH only when distinct appropriate variants exist) and an English fallback as applicable.
4. Do not pretend to have an office in Germany/Austria/Switzerland or claim "Made in Germany" for Pakistani production.
5. Where credible, include import-ready practical information (shipping document types, origin, quote Incoterm process, sizing nomenclature) reviewed by owner; do not quote unsupported customs rates/taxes.
6. Launch country-specific landing pages only where materially different buyer needs, localized examples or verified market services justify them; avoid doorway pages.
7. Track country/query and lead-quality cohorts in GSC/GA4 and refine country priorities after evidence accrues.

## 8. Frontend design, UX and conversion

### Homepage design workstream
- Clear above-the-fold text H1 and immediate RFQ CTA; eliminate generic demo sliders/copy.
- Use authentic, high-resolution but optimized approved garment/factory photos; show recognizable Lederhosen/Dirndl products.
- Visually differentiate men's, women's, kids' and accessory collections (only stocked/real).
- Preserve high legibility: mobile-first type scales, accessible contrast, keyboard focus, descriptive button text, stable header/navigation.
- Header: brand, key categories, About/Capabilities, Request Quote, contact. Keep WhatsApp or direct chat optional after business owner approves number and response staffing.
- Footer: actual business identity, verified contact details, legal/privacy links, live social links, regional service information where true.

### Product/category conversion
- Product RFQ button should capture the selected product or SKU automatically; never make buyers retype product names.
- Collect size/color quantity breakdowns, branding/artwork needs, deadline and shipping destination when appropriate.
- Separate "Request Bulk Quote" from "Discuss a Custom Sample/Development" if owner can honor both.
- Trust modules: transparent response expectations, real quality control checkpoints, packing sample images and approval workflow.
- Use clear content for consumers vs business buyers; hide/alter retail cart/price UI only if owner explicitly selects wholesale-first buying model. Do not break the existing WooCommerce customer purchase journey unknowingly.

### B2B inquiry form (proposed fields)
Required: company, contact person, work email, country, interested category/product, estimated quantity, requirements/message, consent where required. Optional: website/LinkedIn, role, planned date, sizing, fabric/material, branding details, shipping city, secure design upload. Include accessible validation, file size/type limits, honeypot/rate limits, success receipt, no credentials/attachments in public GitHub, SMTP/delivery checks, owner-approved privacy retention.

### Mobile and usability acceptance
- 390 px and 360 px mobile plus 768/1440 desktop browser tests.
- Navigation works without overlay, product filters/quotes remain tappable, images not cropped in a misleading way, forms test successful, no horizontal overflow, no broken images, no PII leaked in page HTML.
- Smoke tests found no mobile horizontal overflow or JavaScript load errors on homepage, but this does not cover every interaction or screen.

## 9. Backend engineering and operational integrations

**Platform:** self-hosted WordPress + WooCommerce + Elementor + WoodMart + LiteSpeed Cache + Smash Balloon Instagram Feed + JetBackup. Existing GitHub Actions scripts allow read-only audits and a confirmed authenticated API connection; direct Elementor/theme writes are NOT proven.

### Access and deployment architecture
- Keep GitHub repository under owner account and operator as collaborator; explicitly audit app installations, collaborators and actions permissions.
- Limit code modifying workflows on the production main branch; do not automatically run an unreviewed push with WordPress admin secrets.
- Create a separate **production-write environment** restricted to an explicitly reviewed main branch and requiring owner review where available. Use a distinct narrowly scoped Application Password; do not reuse the existing admin connection for unattended publishing.
- Back up WordPress database + uploads + theme child-customizations + plugin config to a privately controlled location, and verify a restore before writes. Keep backups private/off public GitHub.
- Avoid direct changes to parent WoodMart/theme or Elementor serialized metadata without a supported migration and restore test. Prefer stable native REST interfaces/approved plugin APIs or WordPress UI under owner authorization.
- Dry-run outputs show exact field diffs, slugs, affected IDs and HTML before publish. Write a manifest for each batch, test one low-risk item, then expand 5 → 20 → remaining verified items after QA.
- If any write fails, stop the batch and rollback; never claim live completion without HTTP + rendered-site + Google tests.

### CRM and enquiry handling
- Reuse existing Contact Form 7 if its configured form and delivery work; otherwise migrate carefully to an equivalent free solution after export.
- Verify SPF/DKIM/DMARC and contact mail delivery, replies, bounce handling and mobile receipt. Never assume an admin email inbox is receiving RFQs just because form shows a success popup.
- Maintain a private lead pipeline: New → Verified → Qualified → Specifications pending → Quoted → Sampling → Negotiation → Order won/lost → Repeat. Restrict buyer contact information and store outside public GitHub.
- Add business-hours/response expectations only after operational confirmation; no unsupported 24/7 live chat claim.
- GDPR/privacy: user consent and disclosure where required; legal policy should be locally reviewed. GA4/marketing tags respect consent; do not send emails, phone numbers or submitted text as analytics event parameters.

### Instagram and social website configuration
- Existing Smash Balloon **Instagram Feed** plugin is installed; not yet confirmed connected or rendering on homepage.
- Owner grants Instagram/Meta OAuth to the plugin or authorizes a legitimate business-manager role. No passwords, access tokens or login cookies to ChatGPT.
- Check connection status and permissions, build a free responsive feed, select 4–8 approved genuine manufacturing/product posts, put feed where it supports trust rather than obstructs RFQ, lazy-load/cached assets and verify mobile rendering/performance.
- Confirm official Instagram and Facebook destinations and legal ownership. Feed display **does not** automatically confer ability to publish Instagram posts/reels. Direct social publishing is a separate approved permission/API workflow.

### Reliability and security
- WordPress, plugins and theme update inventory; check vulnerabilities and version support before any update; test on staging and backup first.
- Remove unused/demo plugins/assets only when not required by WoodMart or WooCommerce.
- Secure login, MFA where available, TLS, REST endpoint authorization, updates, firewall/rate controls, backups, spam protection and scheduled maintenance tests.
- Do not publish exposed debug logs or integration secrets. Restrict uploaded artwork/quote attachments.
- Check WordPress scheduled cron execution and reliable form notifications; audit caching/redirect behavior after every significant change.

## 10. Analytics and buyer-quality scorecard

### Data connections — initial one-time owner permission
- Google Search Console domain property, sitemaps, indexing reports, Performance queries and country/device filters.
- Bing Webmaster Tools, sitemap and IndexNow (free) where correctly configured.
- Google Analytics 4 / Tag Manager only if owner authorizes; test tag count and consent.
- Real RFQ form conversion and private lead records; reconcile GA4 conversions with received enquiries.
- Google Business Profile only if the company meets eligibility and can verify its real business location. Never invent addresses/locations.

### Conversion event taxonomy
- view_product_category
- view_product
- click_request_quote
- start_rfq
- submit_rfq_success (only after server acknowledgment)
- click_whatsapp
- click_email
- click_catalogue
- click_instagram
- qualified_lead (in private CRM; avoid personal data in GA4)

Use anonymous IDs and non-PII product/category tags only. Deduplicate form events; do not fire lead conversions on page loads.

### North-star and supporting KPIs
**North star:** verified, purchase-capable B2B RFQs per 30 days and quote-to-PO progression (not website visitors alone).
- Qualified lead count, qualification rate, median response time, quotes issued, quoted value where internally tracked, sample approvals, orders, repeat orders.
- Non-branded relevant organic clicks and impressions, indexed **commercial** URLs, country-level qualified sessions, keyword intent, CTR changes by page.
- RFQ-start-to-submit success; mobile-to-desktop RFQ conversion; broken submissions or undelivered notifications.
- CWV p75 LCP/INP/CLS, homepage and category performance, 4xx/5xx/canonical errors, schema validation and accessible product media.
- AI referral traffic if directly attributable and manual citation checks on a fixed buyer query panel; do not present model-generated names as verified referrals.

**Targets (QA, not invented business forecasts):** 100% of approved high-priority templates produce unique or appropriate canonical/metadata after rollout; no confirmed irrelevant demo URLs remain intentionally indexable; zero known broken critical RFQ paths; 100% of real lead submissions reach a private destination in test cases; CWV good thresholds where field data permits. Commercial growth targets require an initial 30-day observed baseline.

**Reporting cadence:** weekly technical change log and high-priority URL spot checks; monthly GSC/GA4 + lead-quality review; quarterly content and security audit. GitHub cron can produce public audit summaries, but **must not** expose private conversion data.

## 11. Priority matrix: impact, dependencies, acceptance

| Priority | Work package | Owner/operator split | Definition of done |
|---|---|---|---|
| P0 | Verified restore backup + least-privilege account + GitHub secrets governance | Owner one-time authorization; operator setup/test | Successful isolated restore, private backup, revoked broad credential where feasible |
| P0 | GSC/GA4 ownership and baseline | Owner access approval; operator analysis | Visible verified property and baseline, no fabricated impressions |
| P1 | SEO metadata generator/template repair | Operator, after owner-approved pilot | Rendered title/meta/OG across sample templates; no duplicate output |
| P1 | Canonical and index controls | Operator with owner review for consolidation | 44 missing-canonical URLs reviewed; canonical action log and GSC checks |
| P1 | Duplicate product/title mapping | Operator plus owner product truth review | All 118 affected URLs classified; no erroneous product merges |
| P1 | Homepage H1 / identity / quote CTA | Operator frontend pilot; owner brand facts | Real visible H1, usable RFQ from mobile, no hero/CLS regression |
| P1 | Demo content disposition | Owner approve keep/retire; operator execute | All demo URLs mapped, redirects checked, relevant pages preserved |
| P1 | 22 product-category pages | Operator drafts; owner validates capability | Every priority category helpful, distinct, internally linked, QA'd |
| P1/P2 | 140 product pages | Operator staged updates; owner material/style facts | Accurate title/spec/image/CTA and schema checks, diff logs |
| P2 | Real AEO/GEO knowledge hub | Owner verifies expertise; operator publishes | Original useful guides, source-verified claims, buyer query alignment |
| P2 | German localization | Qualified language review and operator | Complete native-quality pages and reciprocal hreflang |
| P2 | Core Web Vitals and accessibility | Operator | Measured before/after no regression, tested forms/navigation |
| P2 | Instagram feed | Owner OAuth once; operator placement | Authorized live feed, approved imagery, mobile and speed QA |
| P2 | RFQ analytics and lead routing | Owner recipient/process approval; operator tests | Successful test request + server delivery + deduplicated conversion event |
| P2 | Brand entity and sourcing trust | Owner evidence; operator | Real NAP/social/logo, verified process gallery and accurate Organization schema |

## 12. Phased schedule (execution sequence, not guaranteed elapsed time)

### Phase 0 — Day 0–7: Establish safe baseline and credibility
- Verify owner approval, backup/restore and GitHub/WordPress least privilege.
- Connect GSC/Bing, define GA4 and lead metrics; capture current GSC screenshots/exports.
- Inspect WordPress/Elementor/WoodMart theme templates, installed plugins, SEO metadata generation and form delivery.
- Inventory all 211 URL decisions, 118 duplicate-title cases, 44 canonical cases and demo content. Assign P0/P1.
- Draft homepage B2B identity, product category taxonomy and editable SEO template rules.
**Gate:** Backup genuinely restorable, change path tested, source-of-truth owner-approved before live pilot.

### Phase 1 — Day 8–21: Fix systemic search and first RFQ path
- Trial one low-risk page and verify rollback.
- Implement ONE compatible free SEO metadata system; fix page head output across real templates and social preview.
- Correct homepage visible H1 and B2B positioning, working quote CTA and mobile enquiry flow.
- Test one representative product and category, then limited batches for meta/OG/canonical/H1.
- Classify demo content and apply only approved noindex/redirect/retire operations.
- QA all changes with public crawler + browser + validator; submit important corrected URLs to GSC.
**Gate:** Representative templates pass tests, no checkout/lead loss, no false claims.

### Phase 2 — Day 22–45: Commercial content and trust
- Rebuild 22 category descriptions/logic by priority; assess 140 products and repair only verified variants at controlled batch cadence.
- Add product spec/size/material modules, factory/quality/proof where available and RFQ context capture.
- Build About/Manufacturing/Process/Materials/Quality pages grounded in owner evidence.
- Add qualified lead pipeline, email deliverability, conversion events and non-PII analytics.
- Improve imagery/accessibility and performance, avoiding cache regressions.
**Gate:** Priority URLs show correct metadata and relevant B2B content; lead tests pass end-to-end.

### Phase 3 — Day 46–90: International reach and refinement
- Publish first expert-led sourcing/Trachten Q&A guides and link to products.
- Pilot German native-reviewed pages where worthwhile and verified; implement full hreflang pairs.
- Build legitimate brand and directory consistency, original PR/editorial opportunities and relevant trade links (no purchased spam links).
- Configure approved free Instagram feed and measure its speed/conversion effect.
- Use GSC and real leads to adjust keywords and page investment; report month-over-month changes against *actual* baseline.
**Gate:** Real performance and qualified RFQ dashboard, documented improvement and remaining backlog.

## 13. Pilot and scaling protocol

1. Identify one low-risk **existing product or category** with clear owner-approved factual data; capture raw REST JSON and public HTML snapshot.
2. Decide whether the task is content-only (REST supported) or template/theme/SEO plugin configuration (separate test).
3. Prepare proposed before/after field diffs with an owner-reviewed preview, backup ID and a single rollback action.
4. Owner approves the **exact scope** of that first live change, including any theme/SEO plugin installation, user data handling or URL deletion.
5. Execute via approved, protected GitHub environment / supported WordPress mechanism. Verify response, actual rendered frontend, desktop/mobile, canonical/schema, form and related WooCommerce functionality.
6. Record URL, fields, old/new values or snapshots, owner approval, GitHub commit/action ID, proof screenshots and rollback outcome in a **private** audit log where needed.
7. Only after successful pilot, expand to small groups (e.g. 5 then 20) with spot checks. A failing check stops rollout.
8. Back out on broken quotes, checkout, canonical to wrong page, missing title or author data leakage. Review GSC after Google re-crawls; changes do not guarantee rankings.

## 14. Owner approvals needed once, not day-to-day manual work

For a truly operator-run workflow, the owner should approve only access/facts that cannot safely be inferred:
1. Actual Alpen Crew legal business identity and approved public contact/social details, brand assets.
2. Which production, sampling, custom labeling, fabrics, MOQ, QC and delivery capabilities are true (with supporting documents).
3. Verified backup storage/restore and separate least-privileged API user / protected GitHub environment; permission to run approved write workflows.
4. One content/theme pilot and the disposition of demo pages or destructive changes.
5. Official Instagram/Meta account OAuth; GSC/GA4/Bing access where not already linked; RFQ recipient inbox.
6. Any material commercial/policy claims or public customer references.

The operator then handles research, drafting, code changes, auditing, validation, monitoring and reporting within approved scope. No direct account passwords or tokens in chat.

## 15. Risk register and things explicitly NOT to do

- **Public GitHub + admin credential:** Workflow write access can threaten environment secret confidentiality. Fix controls before ongoing production writes.
- **SEO plugin conflict:** Two plugins or theme duplication can generate competing meta tags/canonicals; test plugin/hooks before installation.
- **Overaggressive duplicate removal:** Similar slugs may be meaningful unique stock/style variants; validate with owner and data.
- **SEO mass writing:** AI-generated high-volume thin pages or invented material/certification claims harm trust.
- **Blind redirects:** Do not 301 all unrelated furniture/demo URLs to homepage; use closest relevant legitimate target or proper gone handling.
- **False Google/AI expectations:** Technical completeness does not guarantee indexing, impressions, AI mention or leads.
- **Analytics privacy:** Never publish buyer PII and never collect form contents in GA4 or public GitHub Actions.
- **Meta OAuth confusion:** Instagram feed display does not grant Instagram posting or direct-message control.
- **Free-only discipline:** No paid runner, plugin upgrade, monthly credit service or unnecessary subscription; discuss free-feature limits rather than silently switching paid.
- **Performance regressions:** Check sticky contact widgets, animation, image loading, caches and plugins on both mobile and desktop.

## 16. Source documents and standards

**Alpen Crew owned first-party evidence**
- [Full 211-URL SEO and frontend audit](../reports/2026-11-03-full-211-url-seo-frontend-audit.md)
- [Authenticated WP API capabilities audit](../reports/2026-11-03-wordpress-capabilities.md)
- [Full crawl GitHub Actions](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664612642)
- [WordPress read-only capabilities run](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664880706)
- [Desktop/mobile browser run and screenshots](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41665480937)
- [Master execution prompt](../prompts/alpen-crew-master-b2b-growth-execution-prompt.md)

**Public primary guidance (checked 3 Nov 2026)**
- Google Search Central: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google AI features & website: https://developers.google.com/search/docs/appearance/ai-features
- Google people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Google canonicalization: https://developers.google.com/search/docs/crawling-indexing/canonicalization
- Google snippets/meta descriptions: https://developers.google.com/search/docs/appearance/snippet
- Google Organization schema: https://developers.google.com/search/docs/appearance/structured-data/organization
- Google Product structured data: https://developers.google.com/search/docs/appearance/structured-data/product
- Google product variants: https://developers.google.com/search/docs/appearance/structured-data/product-variants
- Google localized versions: https://developers.google.com/search/docs/specialty/international/localized-versions
- Google Core Web Vitals: https://developers.google.com/search/docs/appearance/core-web-vitals
- Bing IndexNow: https://www.bing.com/indexnow/getstarted
- WordPress Application Passwords: https://developer.wordpress.org/advanced-administration/security/application-passwords/
- Smash Balloon Free Instagram Feed setup: https://smashballoon.com/doc/setting-up-the-free-instagram-feed-wordpress-plugin/

**Change log:**
- 2026-11-03: Master plan generated from verified audits, external standards and identified business goals. Production changes explicitly not authorized under this document alone.
