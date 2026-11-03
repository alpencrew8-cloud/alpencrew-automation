#!/usr/bin/env python3
"""Public B2B enquiry journey audit. No submissions, accounts, credentials, or personal data."""
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, Error

ROOT = "https://alpencrew.com"
PATHS = [
    "/", "/contact-us/", "/shop/", "/product-category/men/",
    "/product-category/women/dirndle/",
    "/product/lederhosen-men-short-green/",
    "/product/womens-german-dirndl-dress-blue-gold/",
]
VIEWS = {"mobile_390": (390, 844), "desktop_1440": (1440, 900)}
CAPTURE_JS = r"""() => {
    const text = e => ((e.innerText || e.textContent || "").trim().replace(/\s+/g," ").slice(0,100));
    const links = Array.from(document.querySelectorAll("a[href]"));
    const ctaPattern = /\b(quote|quotation|inquiry|enquiry|contact|wholesale|bulk|request|custom|message|sample|angebot|anfrage|kontakt)\b/i;
    const actions = links.filter(a => ctaPattern.test(text(a))).slice(0,30).map(a => {
        const raw = a.getAttribute("href") || "";
        let targetKind = "unknown", targetPath = "";
        if (raw.startsWith("mailto:")) { targetKind = "email"; }
        else if (raw.startsWith("tel:")) { targetKind = "telephone"; }
        else {
            try {
                const u = new URL(raw, document.baseURI);
                targetKind = /wa\.me$|whatsapp\.com$/.test(u.hostname) ? "whatsapp"
                  : u.hostname === "alpencrew.com" ? "internal" : "external";
                targetPath = (targetKind === "internal") ? u.pathname : "";
            } catch (_) {}
        }
        return {text: text(a), target_kind: targetKind, target_path: targetPath};
    });
    const formList = Array.from(document.querySelectorAll("form")).slice(0,30).map(f => {
        const fields = Array.from(f.querySelectorAll("input,textarea,select"))
          .filter(el => !["hidden","submit","button","reset"].includes(el.type))
          .map(el => ({
            field_type: (el.getAttribute("type") || el.tagName || "").toLowerCase().slice(0,24),
            field_name: (el.getAttribute("name") || "").slice(0,64),
            required: el.required || el.getAttribute("aria-required") === "true"
        })).slice(0,40);
        const raw = f.getAttribute("action") || "";
        let action_domain = "";
        try {action_domain = new URL(raw, document.baseURI).hostname;} catch (_) {}
        return {
          method: (f.getAttribute("method") || "get").toLowerCase(),
          action_domain: action_domain,
          field_descriptors: fields
        };
    });
    const buttons = Array.from(document.querySelectorAll("button,input[type=submit]"))
      .map(el => text(el) || (el.getAttribute("value") || "").slice(0,60))
      .filter(Boolean).slice(0,30);
    const privacy = links.some(a=>/privacy|datenschutz/i.test((a.innerText || "") + " " + (a.getAttribute("href") || "")));
    return {actions, forms: formList, button_labels: buttons, privacy_link_present: privacy,
      headings: Array.from(document.querySelectorAll("h1")).map(e=>text(e)).slice(0,5)};
}"""


def classify_fields(forms):
    """Classify only public form schema; never capture or print filled field values."""
    tokens = []
    for form in forms:
        for field in form.get("field_descriptors", []):
            tokens.append(field.get("field_name", "").lower())
    joined = " ".join(tokens)
    classes = {
        "business_or_company": r"company|business|organization|organisation|firma",
        "work_email": r"email|e-mail",
        "phone": r"phone|tel|mobile",
        "country": r"country|land",
        "product": r"product|style|garment|item|kategori|category",
        "quantity": r"quant|qty|units|pieces|menge|stück",
        "sizes": r"size|size.run|size_breakdown|grö(ss|ß)e",
        "material": r"fabric|material|stoff",
        "customization": r"brand|logo|embroid|custom|print|veredel",
        "timeline": r"deadline|timeline|delivery|date|liefer",
        "message": r"message|comment|details|notes|anfrage|nachricht"
    }
    return {kind: bool(re.search(pattern, joined, re.I)) for kind, pattern in classes.items()}


def inspect(browser, url, view, width, height):
    p = browser.new_page(viewport={"width": width, "height": height})
    record = {"url": url, "viewport": view}
    try:
        response = p.goto(url, wait_until="domcontentloaded", timeout=30000)
        p.wait_for_timeout(700)
        current = urlparse(p.url)
        if current.hostname != "alpencrew.com" or current.scheme != "https":
            raise ValueError("Redirect to unapproved website")
        payload = p.evaluate(CAPTURE_JS)
        record.update({
            "http_status": response.status if response else None,
            "h1": payload["headings"],
            "cta_count": len(payload["actions"]),
            "cta_sample": payload["actions"][:12],
            "form_count": len(payload["forms"]),
            "form_field_coverage": classify_fields(payload["forms"]),
            "form_methods": sorted(set(f["method"] for f in payload["forms"])),
            "form_action_domains": sorted(set(f["action_domain"] for f in payload["forms"] if f["action_domain"])),
            "privacy_link_present": payload["privacy_link_present"],
            "button_labels": payload["button_labels"][:10],
        })
    except (Error, ValueError) as exc:
        record["error"] = f"{type(exc).__name__}: {str(exc)[:120]}"
    finally:
        p.close()
    return record


def main():
    out = Path("b2b-enquiry-audit-out")
    out.mkdir(exist_ok=True)
    records = []
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            for view, (width, height) in VIEWS.items():
                for path in PATHS:
                    records.append(inspect(browser, ROOT + path, view, width, height))
        finally:
            browser.close()
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "data_classification": "public form schema and public link labels only",
        "no_submissions": True, "no_credentials": True, "production_writes": False,
        "methodology": "Loaded rendered page, inspected link/button labels and blank form field names only",
        "records": records
    }
    (out / "b2b-enquiry-audit.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Alpen Crew — Public B2B buyer enquiry audit", "",
             "Read-only. **No forms submitted**; notification/email delivery remains UNVERIFIED.",
             "Any detected contact CTA must still undergo user-click and delivery testing after security gate.", "",
             "| URL | View | HTTP | CTAs | Forms | Company | Email | Qty | Product | Privacy link |",
             "|---|---|---:|---:|---:|---|---|---|---|---|"]
    for r in records:
        fields = r.get("form_field_coverage", {})
        lines.append("| " + " | ".join([
            r["url"], r["viewport"], str(r.get("http_status", "-")),
            str(r.get("cta_count", "-")), str(r.get("form_count", "-")),
            "Y" if fields.get("business_or_company") else "N",
            "Y" if fields.get("work_email") else "N",
            "Y" if fields.get("quantity") else "N",
            "Y" if fields.get("product") else "N",
            "Y" if r.get("privacy_link_present") else "N"
        ]) + " |")
    lines.extend(["", "## Interpretation", "",
                  "- A CTA count does not prove a useful or functional quotation path.",
                  "- An input field name does not prove validation, delivery, spam protection, or server-side storage.",
                  "- Absent named fields are signals to investigate, not proof no custom JavaScript form exists.",
                  "- No customer/buyer data was retrieved or transmitted."])
    (out / "b2b-enquiry-audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
