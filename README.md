# Alpen Crew — WordPress SEO Automation

Owner: `alpencrew8-cloud` · Website: https://alpencrew.com

This repository uses **free standard GitHub-hosted Actions** and a **read-only public SEO sampler**. No site administrator credentials, paid subscriptions, or plugins are needed for the first phase.

## Run the first audit

1. Open [GitHub Actions](https://github.com/alpencrew8-cloud/alpencrew-automation/actions).
2. Click **Alpen Crew — Free Read-Only SEO Audit** on the left.
3. Click **Run workflow** → choose `main` → **Run workflow**.
4. Open the completed run → **Summary** to see the URL sample and SEO flags.

It also runs automatically every Monday at 05:00 UTC (10:00 PKT) and when the approved SEO scanner/workflow files are updated on `main` (GitHub may delay scheduled runs).

**First verified automatic run:** [Run #1 — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41660001499). The recorded findings are in [2026-11-03 public SEO audit](reports/2026-11-03-public-seo-audit.md).

## Scope and safety

- Reads only public `/wp-json/`, `/robots.txt`, public XML sitemaps, and up to 25 pages.
- Tests a sample for titles, meta descriptions, canonicals, H1 counts, Open Graph and JSON-LD.
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
