# Alpen Crew — 211-URL Technical SEO + Frontend Audit (2026-11-03)

**Evidence:** [Full public sitemap crawl — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664612642), [WordPress API capability audit — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664880706), [Desktop/mobile browser audit — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41665480937).

**Execution:** Read-only. No credentials used in public/browser scans; authenticated capability scan used owner-managed GitHub environment secrets and GET requests only. No site changes or paid services.

## Scope

- 211 unique public XML sitemap URLs checked, including homepage.
- 140 product URLs, 22 product-category URLs, 13 blog/archive URLs and 36 other URLs.
- Successful public WordPress REST API and robots.txt responses (HTTP 200).

## Technical findings

| Finding | Observed count |
|---|---:|
| Missing meta description | 211 of 211 |
| Missing Open Graph title | 211 of 211 |
| URLs sharing duplicate HTML titles | 118 |
| Missing canonical link element | 44 |
| Pages without an H1 | 28 |
| No JSON-LD detected | 6 |
| HTML meta noindex | 3 |
| Titles exceeding 65 characters (review threshold) | 1 |

### Clarifications

- Three meta noindex URLs: `/cart/`, `/checkout/`, `/my-account/`. This is **appropriate for transaction/account pages**; do not automatically remove noindex.
- Missing canonical tags are concentrated on product-category and archive pages; includes `/shop/` and other site pages. Do not canonicalize unrelated products to a common URL.
- Duplicate titles include products that may represent distinct variants. **Keep distinct valid variants** and write truthful differentiators; do not mass merge/delete products on slug similarity alone.
- JSON-LD absent on homepage/about/contact and certain utility pages; not all need schema. The audited product pages generally had detectable JSON-LD; do not duplicate it.

## Demo/non-apparel content requiring owner-reviewed cleanup

The public sitemap includes unrelated WoodMart/demo or legacy content, including:

- `/2021/08/26/minimalist-japanese-inspired-furniture/`
- `/category/furniture/`, `/tag/furniture/`, `/project-cat/furniture/`
- `/portfolio/` and multiple lorem-ipsum portfolio entries
- `/sample-page/`, `/home-fashion-color/`

**Do not delete immediately.** Confirm content ownership, existing traffic/backlinks and internal references, then choose appropriate updating, noindex, redirect or deletion and preserve a restore backup.

## Real desktop/mobile frontend audit

| Check | Desktop | Mobile |
|---|---|---|
| Homepage HTTP | 200 | 200 |
| H1 elements | 0 | 0 |
| Meta description | Missing | Missing |
| Image tags | 27 | 27 |
| Images with empty/missing alt | 25 | 25 |
| Visibly broken images | 0 | 0 |
| Horizontal overflow | Not detected | Not detected |
| JavaScript page errors | 0 | 0 |
| Instagram links | 1 | 1 |
| Facebook links | 1 | 1 |
| WhatsApp links | 0 | 0 |
| Instagram feed markup | Not detected | Not detected |

These are page-load smoke tests; they do not certify every interaction. Decorative images may appropriately use empty alt.

Screenshots: [frontend workflow, artifact section](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41665480937).

## Authenticated WordPress capabilities

- Pages, posts, media and WordPress post types return HTTP 200 in edit context.
- WooCommerce products API HTTP 200; `product` and `elementor_library` types are REST-exposed.
- Elementor, WooCommerce, Smash Balloon Instagram Feed, LiteSpeed Cache and JetBackup detected.
- No detected standard installations of Yoast, Rank Math, AIOSEO or SEOPress.
- These read permissions **do not prove** that Elementor layout, theme options, SEO meta or product writes are available.

## Fix priority and safety

1. **P0 access and rollback:** verify a working restore backup; replace shared administrator Application Password with a dedicated limited-permission automation user; enforce review of GitHub Actions code that can access secrets.
2. **P1 SEO foundation:** choose an appropriate **free** SEO plugin/metadata integration; verify actual frontend meta output, canonical behavior and OG tags on an approved low-risk page before templated rollout.
3. **P1 B2B landing pages:** give homepage, product categories and products accurate H1, unique titles and useful business descriptions, avoiding unverified manufacturing claims.
4. **P1 unwanted demo content:** audit all unrelated demo/posts/portfolios for traffic/backlinks and remove/noindex/redirect only after review.
5. **P2 images and frontend:** meaningful product alt text, strong contact/quote CTAs, mobile navigation, inquiry flow, caching and render checks.
6. **P2 Instagram feed:** check plugin's settings; account owner must approve official Instagram/Meta OAuth connection, then place and visually test feed on approved website area.
7. **P2 verify:** recrawl and compare before/after, then request Google Search Console indexing where appropriate.

**Production writes:** NOT ENABLED. Specific owner approval, verified recovery plan and a small before/after pilot are required before changing published content.
