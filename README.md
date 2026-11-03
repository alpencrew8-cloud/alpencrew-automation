# Alpen Crew — WordPress SEO Automation

Owner: `alpencrew8-cloud` · Website: https://alpencrew.com

This repository uses **free standard GitHub-hosted Actions** and a **read-only full-sitemap public SEO auditor**. No site administrator credentials, paid subscriptions, or plugins are needed for the first phase.

## Run the first audit

1. Open [GitHub Actions](https://github.com/alpencrew8-cloud/alpencrew-automation/actions).
2. Click **Alpen Crew — Free Read-Only SEO Audit** on the left.
3. Click **Run workflow** → choose `main` → **Run workflow**.
4. Open the completed run → **Summary** to see the URL sample and SEO flags.

It also runs automatically every Monday at 05:00 UTC (10:00 PKT) and when the approved SEO scanner/workflow files are updated on `main` (GitHub may delay scheduled runs).

**First verified automatic run:** [Run #1 — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41660001499). The recorded findings are in [2026-11-03 public SEO audit](reports/2026-11-03-public-seo-audit.md).

## Scope and safety

- Reads only public `/wp-json/`, `/robots.txt`, public XML sitemaps, and up to 260 sitemap-discoverable URLs (211 checked successfully on 2026-11-03).
- Checks titles, duplicate titles, meta descriptions, canonicals, H1 counts, Open Graph and JSON-LD on sitemap-discoverable URLs.
- **Does not** edit WordPress, publish content, update plugins, crawl all products, or infer real Google traffic.
- Uses only `ubuntu-latest`, Python standard library and GitHub's official checkout/setup-python actions.
- Never commit passwords, WordPress Application Passwords, access tokens, customer lists, orders, private backups or environment files to this public repository.
- Before a later *write* phase, configure credentials only through **Settings → Secrets and variables → Actions**, add dry-run validation, and obtain owner approval.

## Files

- [Read-only audit script](scripts/public_seo_audit.py)
- [GitHub Actions workflow](.github/workflows/public-seo-audit.yml)
- [Future authenticated API connectivity check (not yet configured)](scripts/wordpress_auth_healthcheck.py)
- [First verified audit report](reports/2026-11-03-public-seo-audit.md)

For actual WordPress editing through the REST API, a separate approved integration and secure authentication will be required. That capability is **not yet enabled**.

## Free authenticated WordPress connection — next phase

**Connection verified on 2026-11-03:** [GitHub Actions authentication test — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41663708582). WordPress accepted the Application Password via the authenticated REST API. No WordPress content was changed. The [API test workflow](.github/workflows/wordpress-auth-test.yml) is manual-only again. **Automated website editing and publishing remain disabled** pending dry-run, backups, owner-reviewed scope and access-control checks.

Security: this is a public repository with collaborators who have write access. Do not assume encrypted environment secrets alone protect privileged WordPress access from changes to workflow code. Restrict repository write access, review changes, and use a dedicated least-privileged WordPress account for any future production automation.


## Full site, frontend and API audits — 2026-11-03

- [Full 211-URL SEO audit and repair priorities](reports/2026-11-03-full-211-url-seo-frontend-audit.md)
- [WordPress API and plugin capability audit](reports/2026-11-03-wordpress-capabilities.md)
- [Desktop and mobile screenshot test](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41665480937)
- [Read-only frontend browser script](scripts/frontend_smoke_test.py)

No WordPress production writes have been performed; owner-reviewed approval and backup verification are required first.

## Execution update: 3 November 2026

**Work performed through the connected ChatGPT GitHub collaborator, with no production edits:**

- [Draft PR #1 — owner-reviewed safety gate and implementation](https://github.com/alpencrew8-cloud/alpencrew-automation/pull/1).
- [Execution batch 01 with exact tested URLs, commits, rollout gates and statuses](reports/2026-11-03-execution-batch-01.md).
- [SEO public before-snapshot GitHub Actions — success, 3/3 tests, 7/7 URLs HTTP 200](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41699002516).
- [Responsive category/product browser QA — success, 10/10 page loads HTTP 200](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41699809581).
- [Security/restore requirements](docs/production-safety-gate.md); [non-live homepage content/SEO pilot](proposals/2026-11-03-homepage-b2b-seo-pilot.md).

**Do not confuse prepared GitHub code with a deployed WordPress fix.** The owner must configure branch and environment controls and verify private full-site restoration before approving a live pilot.

## Execution batch 02 — 4 November 2026

Read the [complete second execution report](reports/2026-11-04-execution-batch-02.md) for exact statuses, inspected URLs, test output and production blockers.

- [Buyer quote/contact journey audit 41701613912](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41701613912) **success**, 14/14 HTTP 200 and 3/3 tests. Contact form did not expose the major business-qualification fields in tested renderings.
- [Homepage SEO exact before/after proposal 41701959078](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41701959078) **success**, 4/4 offline tests. Owner-review manifest produced; **not live**.
- [WordPress RFQ plugin candidate](plugins/alpencrew-b2b-rfq/README.md) (first-party shortcode, privacy/recipient gate, WooCommerce product context, anti-spam); [PHP offline QA 41702672610](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41702672610) **success**. **Not installed**.
- [PR #1](https://github.com/alpencrew8-cloud/alpencrew-automation/pull/1) remains owner-review pending, branch \`main\` unprotected, and no production WordPress edits have been made.

**P0 gate remains mandatory:** owner-enabled GitHub protections and independent reviewer, restorable off-site WordPress backup, dedicated lower-privilege credentials, exact pilot scope approval and rollback tests.
