# Alpen Crew — One-time secure WordPress connection

## Already prepared

- GitHub public SEO scanner: successful first run.
- WordPress REST API: HTTP 200 publicly.
- WordPress **Application Passwords**: section visibly available to the owner.
- Secure read-only auth workflow: [.github/workflows/wordpress-auth-test.yml](../.github/workflows/wordpress-auth-test.yml)
- No password saved to GitHub or ChatGPT yet.

## 1 — Owner: create GitHub environment (Free for public repository)

Log into GitHub as **alpencrew8-cloud**.

1. Open [Repository environments](https://github.com/alpencrew8-cloud/alpencrew-automation/settings/environments).
2. Click **New environment**.
3. Enter **alpencrew-wordpress**, then **Configure environment**.
4. Restrict **Deployment branches and tags** to **Selected branches and tags**, and add only \`main\`.
5. Under **Environment secrets**, add the two secrets in the following steps.
6. Do not add any passwords to repository files, issues, pull requests, or chat.

GitHub Free public repos support environment secrets; if this repo is switched to private while owner remains on GitHub Free, these environment secrets/protections will not be accessible.

## 2 — Owner: create a dedicated WordPress Application Password

In [Alpen Crew WordPress Admin](https://alpencrew.com/wp-admin/), using the **dedicated admin user's account**:

1. Open **Users → Profile** (or **Users → All Users → Edit** for the dedicated admin).
2. Find **Application Passwords**.
3. Under new application password name, enter **alpencrew-github-api**.
4. Click **Add New Application Password**.
5. Copy the one-time password privately. Never send the value to ChatGPT or commit it to GitHub.

If creating a new, lower-privilege WordPress user for future API work, choose roles compatible with the tasks. For now this step only verifies a user's identity, not authorization for editing products or settings.

## 3 — Owner: save exactly two GitHub Environment Secrets

In the **alpencrew-wordpress** GitHub environment under **Environment secrets**:

- Secret **WP_USERNAME**: the *exact WordPress login username* of the user whose Application Password was generated (not their display name, and not their GitHub username).
- Secret **WP_APPLICATION_PASSWORD**: the one-time **WordPress Application Password** from the previous step (not the user's regular WP login password).

The secret values are not shown after saving. Use separate entries; never paste either into repository code, .env files, the README, issues, or ChatGPT.

## 4 — Test

Open [Secure WordPress API Test workflow](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/workflows/wordpress-auth-test.yml), choose **Run workflow → main**. The job is read-only; it checks \`/wp-json/wp/v2/users/me?context=edit\`. A successful run prints only **SUCCESS**; no credentials, private user data or changes.

If it reports **HTTP 401**, confirm the secret username/password and that the hosting server passes the Authorization header. If **HTTP 403**, check permissions/security plugins. If **NOT_CONFIGURED**, confirm both secrets exist in the **environment** rather than elsewhere.

## Security and control

- This is a **public repository**: all code is visible, but GitHub environment secrets are not printed.
- Anyone with GitHub write access can modify Actions code and potentially misuse secrets; restrict collaborators and review workflow changes.
- Do not enable automatic site writes until a separate dry-run, backup, permissions review and owner approval have succeeded.
- Future production writes should use a **separate protected environment** with owner approval.
- Owner can revoke WordPress Application Password in **Users → Profile → Application Passwords** at any time.

No paid plugin, browser service or new GitHub subscription is required for this test on a public GitHub repository.
