# Alpen Crew — production security and restoration gate (3 Nov 2026)

**Site:** https://alpencrew.com  
**Owner:** alpencrew8-cloud  
**Operator:** irhaapparelsofficial-ctrl (GitHub write collaborator)  
**Status:** BLOCKED for all production writes. This document does not authorize deployment.

## Verified technical facts

- Repository is **public**. Operator has **write**, not admin, rights.
- Default branch \`main\` returned \`protected: false\`; repository rulesets API returned an empty list.
- Existing WordPress Actions use GitHub environment \`alpencrew-wordpress\` and credentials \`WP_USERNAME\` and \`WP_APPLICATION_PASSWORD\`.
- The current Application Password is associated with a WordPress **administrator**, per owner report. An earlier WordPress GET authentication and capability read succeeded; no write proof exists.
- Existing WordPress workflows are manual-only, but that alone does not prevent a collaborator from changing a workflow when \`main\` is unprotected.
- JetBackup was detected as installed. **A current usable off-site backup and successful restore have not been verified.**
- Environment rules, authorized reviewers, credential scope, backup contents and restore operation were **not** readable through available GitHub collaborator tools; do not infer their configuration.
- The separate \`seo-pilot-readonly.yml\` workflow uses **zero credentials**, GitHub token \`contents: read\` and exclusively public GET requests.

## Owner-controlled prerequisites — complete before any production POST/PUT/PATCH/DELETE

1. **Immediate credential containment:** stop dispatching workflows with the administrator Application Password until reviewed. Consider revoking that Application Password in WordPress and replacing the environment secret with a dedicated account once ready. Preserve normal human administrator access.
2. **Repository control:** owner reviews collaborators and limits write privileges; enables pull-request approval requirements and default-branch protection/rulesets available to the GitHub plan. Require owner approval for changes to \`.github/workflows/**\` and \`scripts/**\` that could touch live credentials. Do not rely on a PR description or a self-authored code check as a security boundary.
3. **Environment control:** owner reviews \`Settings → Environments → alpencrew-wordpress\`, the allowed deployment branches and required reviewers where supported. Ensure a contributor who can edit workflow code cannot self-approve access to administrator-level secrets. No secure enforcement can be proven from this repository alone.
4. **Least privilege:** create an individual WordPress automation user with only capabilities required for each approved operation; verify accessible REST routes with GET and dry run first. Keep the secret exclusively in the owner-controlled GitHub environment. Never print/commit/copy it to chat.
5. **Restoration:** create private backup of database, WordPress uploads, theme/child theme, plugins, site settings and WooCommerce configuration. Run an isolated restore and test representative pages and products. Record where backup and restore evidence is stored **privately**, not in GitHub.
6. **Scope and approvals:** owner supplies page/product IDs, an exact before/after change manifest, intended WordPress publication state, and a go/no-go approval for the initial single-page pilot.
7. **Rollback:** capture precise current REST fields and rendered page before applying. Ensure the operator can restore the approved pilot by documented, previously tested method. Stop automatically on unexpected response.
8. **Post-deployment QA:** verify live HTTP, page HTML title/description/OG/canonical/H1, desktop/mobile display, checkout isolation, working quote form and no caching regression. Run public baseline again; record URLs and timestamps.

## Prohibited until gate passes

- Admin credentials in workflows that can run unreviewed contributions.
- WordPress plugin/theme installation, deactivation, mass SEO writes, Elementor metadata edits, deletions, redirects or WooCommerce product edits.
- Automatic production Actions triggers, owner-free approval, and GitHub-based storage of private backup or buyer personal data.

## First safe pilot

**Candidate:** homepage editorial metadata/H1 and a separately owner-verified B2B call-to-action, using the implementation spec at \`proposals/2026-11-03-homepage-b2b-seo-pilot.md\`. No live edit is approved or executed. Product/category URLs are for read-only regression tests, not automatic editing.

### Owner approval record

- Owner approval: **NOT RECEIVED** for specified production change manifest.
- Restoration evidence: **NOT VERIFIED**.
- Restricted WordPress credentials: **NOT VERIFIED**.
- GitHub branch/environment protections: **NOT VERIFIED**.
- Rollback test: **NOT VERIFIED**.
- Production edit authorization: **NO**.

## GitHub Free owner setup (public repo)

This repository is public; [GitHub branch protection](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) and [required environment reviewers](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) can be used on GitHub Free for public repositories.

- Owner → Repository **Settings → Branches**: protect \`main\`; require pull request and owner approval; block direct pushes/force-pushes and branch deletion as supported. Owner should verify the effective rules after saving.
- Owner → **Settings → Environments → alpencrew-wordpress**: configure required reviewer \`alpencrew8-cloud\`, block self-approval where supported and permit only the intended protected deployment branch. A collaborator's approval must not substitute for independent owner approval.
- Review \`.github/CODEOWNERS\` in PR #1 as an additional review request. It is **not** enforcement until appropriate branch protection is enabled.
- Keep the existing privileged workflow secret disabled or unexposed until both the owner review gate and credential reduction have been verified.

## Quote form and homepage owner-review gate — batch 02

- [Homepage metadata before/after manifest](../scripts/seo_pilot_manifest.py) and [recorded verified run](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41701959078) are **PREPARED only**.
- [RFQ shortcode candidate](../plugins/alpencrew-b2b-rfq/README.md) passed offline syntax/contract checks but **has not been installed**. Owner must confirm whether to extend the current contact-form integration or adopt this optional shortcode, and configure a verified recipient mailbox and a published privacy page.
- Do **not** move stored or transmitted real buyer details into GitHub logs/artifacts. Test only on private staging with synthetic enquiries until a lawful handling and secure notification path is validated.
- No production change can be treated as complete until live frontend verification and the recipient's successful test inbox receipt are proven.
