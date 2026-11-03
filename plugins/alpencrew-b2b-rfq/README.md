# Alpen Crew wholesale RFQ — WordPress staging candidate

**Status: PREPARED / NOT INSTALLED / NOT LIVE.**
This is an optional native WordPress plugin candidate for a reviewed first-party bulk-quotation form. It is not a replacement for an existing working contact form without owner approval and compatibility testing.

## What exists in code

- Shortcode: \`[alpencrew_bulk_quote]\` (must be intentionally placed on an owner-approved page).
- WordPress **Settings → Alpen Crew RFQ**: administrator-configured company recipient address; no destination is hardcoded or invented.
- Form inputs: company, buyer name, work email, website, country, product/style, quantity, size breakdown, fabrics/material, custom branding, delivery date/location, extra message, privacy consent.
- WooCommerce product-aware prefill: a published \`product\` page or same-site link \`?product_id=<published-number>\`. Product IDs are public catalog references, not PII. Invalid/unpublished product IDs do not prefill.
- Uses standard \`admin-post.php\` handler, WordPress nonce validation, spam honeypot, capped and sanitized strings, integer quantity validation and a short-lived salted-IP-hash rate limit.
- Mail goes only to owner-configured address; buyer email is a validated reply-to. No leads/orders are written to public GitHub.
- Fail closed: does not display a working form until a valid owner email AND an official WordPress privacy policy page are configured.
- No attachments, payment, inventory edits, CRM sync, outgoing buyer confirmation, order creation or third-party tracking in this candidate.

## Required pre-installation conditions

1. Complete [owner-controlled WordPress backup/restoration and GitHub security gate](../../docs/production-safety-gate.md). The plugin file being in GitHub does **not** install it on WordPress.
2. Owner approves exact UX/form scope and decides whether to **extend the existing form plugin** or use this candidate. Avoid two competing RFQ forms.
3. Confirm active WordPress/PHP version, actual form plugins, WoodMart/Elementor template path and LiteSpeed cache behavior on an isolated staging copy.
4. Configure WordPress privacy policy, business-owned RFQ receiving mailbox, mail sender/SMTP and recipient; these are owner-controlled settings. Never share them in GitHub or a chat.
5. On staging, exclude RFQ page from full-page cache (or prove nonce freshness despite caching). Confirm cookies/consent and privacy disclosures.
6. Verify email delivery **in the recipient inbox**, not only \`wp_mail()\` returning true. Check errors, bounce handling and spam folder with authorized test data.
7. Test mobile/desktop, accessible labels, keyboard navigation, repeat submission, malicious fields, real product-aware URL, size/quantity validation, form errors, rate limits and privacy link.
8. Review retention/legal requirements before collecting real buyers' personal information.
9. Record before/after and rollback, then separately authorize a low-risk pilot URL. Do not enable this globally.

## Verified offline QA

- [GitHub Actions PHP QA run 41702672610 — success](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41702672610)
- PHP syntax check: passed.
- Offline stub checks: valid/invalid recipient, privacy gate, text sanitation, rejection of array values, required form field schema, nonce presence, published product prefill, invalid product ID rejection.
- These are **offline** tests; WordPress runtime, live email delivery, theme rendering, permissions and real content are not yet tested.

## Why this is needed

[Read-only B2B audit 41701613912](https://github.com/alpencrew8-cloud/alpencrew-automation/actions/runs/41701613912) visited homepage, contact, shop, one men's category, one Dirndl category and two product pages in mobile/desktop. Existing links primarily direct buyers to \`/contact-us/\`. The observed contact form contains email/phone/message fields, but no form fields identified as company, quantity, product, size run or other bulk specifications. Two product pages exposed email/message-style inputs. No complete bulk-RFQ field schema was observed. **This does not prove mail delivery is broken**; no forms were submitted.
