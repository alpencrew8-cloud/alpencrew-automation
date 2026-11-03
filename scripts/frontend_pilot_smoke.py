#!/usr/bin/env python3
"""Browser-only responsive QA for five public Alpen Crew URLs. No clicks, logins or writes."""
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright, Error

SITE = "https://alpencrew.com"
PATHS = [
    ("/", "home"),
    ("/product-category/men/", "category-men"),
    ("/product-category/women/dirndle/", "category-dirndl"),
    ("/product/lederhosen-men-short-green/", "product-lederhosen"),
    ("/product/womens-german-dirndl-dress-blue-gold/", "product-dirndl"),
]
VIEWPORTS = {"mobile": (390, 844), "desktop": (1440, 900)}


def inspect(browser, path, label, width, height, mode, output):
    page = browser.new_page(viewport={"width": width, "height": height},
                            device_scale_factor=1)
    errors = []
    page.on("pageerror", lambda error: errors.append(str(error)[:200]))
    url = SITE + path
    result = {"url": url, "viewport": mode, "width": width}
    try:
        response = page.goto(url, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_timeout(900)
        current = urlparse(page.url)
        if current.hostname != "alpencrew.com" or current.scheme != "https":
            raise ValueError("Unexpected browser destination outside audited domain")
        result["http_status"] = response.status if response else None
        result["render"] = page.evaluate("""() => {
          const all = Array.from(document.images);
          const visible = all.filter(img => img.getClientRects().length > 0);
          const links = Array.from(document.querySelectorAll('a[href]'));
          const quote = links.filter(a =>
            /quote|wholesale|bulk|inquir|enquir|contact/i.test(
              (a.innerText || '') + ' ' + a.getAttribute('href')));
          return {
            title: document.title,
            h1_count: document.querySelectorAll('h1').length,
            h1_text: Array.from(document.querySelectorAll('h1')).map(
              h => (h.innerText || '').trim()).slice(0, 3),
            horizontal_overflow: document.documentElement.scrollWidth > innerWidth + 3,
            image_count: all.length,
            visible_broken_images: visible.filter(
              img => img.complete && img.naturalWidth === 0).length,
            visible_images_missing_alt_including_decorative: visible.filter(
              img => !(img.getAttribute('alt') || '').trim()).length,
            quote_or_contact_links: quote.length,
            forms: document.querySelectorAll('form').length,
            whatsapp_links: links.filter(a => /wa\.me|api\.whatsapp\.com/i.test(a.href)).length
          };
        }""")
        png = output / f"{label}-{mode}.png"
        page.screenshot(path=str(png), full_page=False, timeout=15000)
        result["screenshot"] = png.name
    except (Error, ValueError) as exc:
        result["error"] = f"{type(exc).__name__}: {str(exc)[:180]}"
    result["javascript_page_error_count"] = len(errors)
    page.close()
    return result


def main():
    out = Path("frontend-pilot-out")
    out.mkdir(parents=True, exist_ok=True)
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            for name, (w, h) in VIEWPORTS.items():
                for path, label in PATHS:
                    results.append(inspect(browser, path, label, w, h, name, out))
        finally:
            browser.close()
    report = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "credentials_used": False, "wordpress_writes": False,
        "screenshots": "above-fold only; public page, no submissions",
        "checks": results
    }
    (out / "frontend-pilot.json").write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Alpen Crew — read-only product/category browser QA", "",
             "| Page | View | HTTP | H1 | Overflow | Broken images | Contact/quote links | JS errors |",
             "|---|---|---:|---:|---|---:|---:|---:|"]
    for r in results:
        ui = r.get("render", {})
        lines.append("| " + " | ".join([
            r["url"], r["viewport"], str(r.get("http_status", "error")),
            str(ui.get("h1_count", "-")), str(ui.get("horizontal_overflow", "-")),
            str(ui.get("visible_broken_images", "-")),
            str(ui.get("quote_or_contact_links", "-")),
            str(r.get("javascript_page_error_count", "-"))
        ]) + " |")
    print("\n".join(lines))
    print("\nRead-only. Screenshots and JSON available in the run artifact.")
    (out / "frontend-pilot.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
