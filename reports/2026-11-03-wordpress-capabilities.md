# Alpen Crew — WordPress API Capability Audit (2026-11-03)

Verified via [GitHub Actions run](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41664880706), successful; HTTPS Basic Auth using an owner-stored WordPress Application Password. **GET only**; no site content edited, no credentials displayed.

## Read-only API endpoints

| Capability tested | Result |
|---|---|
| WordPress pages (context=edit) | HTTP 200 |
| WordPress posts (context=edit) | HTTP 200 |
| WordPress media (context=edit) | HTTP 200 |
| WordPress post types (context=edit) | HTTP 200 |
| WordPress plugins inventory | HTTP 200 |
| Active WordPress theme inventory | HTTP 200 |
| WooCommerce products | HTTP 200 |

### Exposed post types

- `page`: yes
- `post`: yes
- `product`: yes
- `elementor_library`: yes
- `product_cat`, `woodmart_slide`, `woodmart_sidebar`: not observed as post types (absence alone does not prove feature absence; taxonomies differ)

### Installed plugin families

- WooCommerce, Elementor, Smash Balloon Instagram Feed, LiteSpeed Cache and JetBackup: detected.
- Yoast, Rank Math, AIOSEO and SEOPress: not detected under their standard plugin slugs.

**What this does not prove:** POST/PUT write permissions, SEO metadata field mutability, Elementor internal layouts, WoodMart theme options, Instagram account connectivity, a restorable backup, sitewide indexing status or any social publishing permission.

## Immediate implementation consequences

1. Build a backup/revision verification and an explicit WordPress **dry-run** before changing production data.
2. Evaluate SEO metadata support: no detected major SEO plugin; avoid assuming custom post meta updates will produce frontend HTML tags.
3. WooCommerce products REST route is readable; test content edits only on owner-approved low-risk item, with precise before/after and rollback.
4. Elementor/WoodMart frontend changes may require WordPress-specific data-layer access and visual checks; standard page REST does not guarantee complete design editing.
5. Smash Balloon can display a feed, but initial Instagram/Meta OAuth requires account owner authorization. Never request login password/token in chat.
6. GitHub repository is **public** and a collaborator has write permission: WordPress admin's environment secret should be replaced with dedicated least-privilege credentials before enabling ongoing production writes.

## Run-mode security

[WordPress API capability audit workflow](../.github/workflows/wordpress-capability-audit.yml) reverted to **manual-only** after this one-time successful test. Full SEO crawl and weekly public checks do not require WordPress credentials.
