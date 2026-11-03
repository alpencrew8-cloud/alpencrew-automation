#!/usr/bin/env python3
"""Generate a strict before/after homepage SEO proposal. No credentials or WordPress writes."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from scripts.seo_baseline_pilot import snapshot

URL = "https://alpencrew.com/"
TARGET = {
    "title": "Wholesale Lederhosen & Dirndl | Alpen Crew",
    "h1": "Bavarian & Trachten Clothing for Wholesale Buyers",
    "meta_description": (
        "Explore Alpen Crew's Lederhosen, Dirndl, traditional shirts and accessories. "
        "Share your styles, quantities and sizes to discuss a business sourcing enquiry."
    ),
    "og_title": "Alpen Crew | Bavarian & Trachten Clothing for Business Buyers",
    "og_description": (
        "Discover traditional-wear product styles and contact Alpen Crew "
        "to discuss business sourcing requirements."
    ),
}


def make_manifest(before):
    if before.get("url") != URL or before.get("http_status") != 200:
        raise ValueError("Live homepage HTTP 200 and exact URL are required")
    if before.get("meta_noindex"):
        raise ValueError("Homepage unexpectedly reports noindex; investigate before proposing changes")
    canonicals = before.get("canonicals", [])
    if len(canonicals) != 1 or canonicals[0].rstrip("/") != URL.rstrip("/"):
        raise ValueError("Homepage canonical changed; investigate before proposing changes")

    present = {
        "title": before.get("title", ""),
        "h1": before.get("h1", []),
        "meta_description": before.get("meta_descriptions", []),
        "og_title": before.get("og_titles", []),
        "og_description": before.get("og_descriptions", []),
        "canonical_preserved": canonicals[0],
    }
    changes = []
    for field in ("title", "h1", "meta_description", "og_title", "og_description"):
        changes.append({"field": field, "before": present[field], "proposed_after": TARGET[field]})
    immutable_before = json.dumps(present, ensure_ascii=False, sort_keys=True)
    return {
        "status": "PREPARED — OWNER APPROVAL REQUIRED; NOT LIVE",
        "live_url": URL,
        "read_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "before_public_metadata_sha256": hashlib.sha256(immutable_before.encode()).hexdigest(),
        "checks_passed": ["HTTP 200", "one homepage self canonical", "no homepage noindex"],
        "changes": changes,
        "must_preserve": ["existing homepage canonical", "functional navigation",
                          "approved images", "real business contact details",
                          "no invented business facts"],
        "needs_owner_verification": ["homepage positioning", "quote CTA destination",
                                    "WordPress Elementor/WoodMart implementation path",
                                    "restorable private backup", "restricted credentials",
                                    "GitHub branch/environment protection",
                                    "rollback test"],
        "wordpress_write_executed": False,
        "production_deployment_authorized": False,
    }


def main():
    before = snapshot(URL)
    manifest = make_manifest(before)
    out = Path("seo-proposal-out")
    out.mkdir(exist_ok=True)
    (out / "homepage-before-after.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Alpen Crew — homepage exact before/after draft", "",
             "**PREPARED. NOT A LIVE FIX. Owner and safety gate approval required.**", "",
             f"URL: {URL}", "",
             "| Field | Before | After (proposal only) |",
             "|---|---|---|"]
    for change in manifest["changes"]:
        old = change["before"]
        if isinstance(old, list):
            old = "; ".join(old) if old else "(missing)"
        lines.append("| " + change["field"] + " | " + str(old).replace("|", "\\|")
                     + " | " + change["proposed_after"].replace("|", "\\|") + " |")
    lines.extend(["", f"Before metadata SHA-256: {manifest['before_public_metadata_sha256']}", "",
                  "Do not deploy until a safe WP API/theme editing path and backup restore have been proven."])
    (out / "homepage-before-after.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
