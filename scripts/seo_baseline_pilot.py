#!/usr/bin/env python3
"""Alpen Crew public SEO before-snapshot. GET-only, credential-free, bounded."""
import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

SITE = "https://alpencrew.com"
PILOT_URLS = (
    SITE + "/",
    SITE + "/product-category/men/",
    SITE + "/product-category/women/",
    SITE + "/product-category/children/",
    SITE + "/product/lederhosen-men-short-green/",
    SITE + "/product/womens-german-dirndl-dress-blue-gold/",
    SITE + "/cart/",
)
MAX_BYTES = 2_000_000


def valid_url(url):
    u = urlsplit(url)
    return (u.scheme == "https" and u.hostname == "alpencrew.com"
            and not u.username and not u.password and u.port in (None, 443))


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Metadata(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title_parts = []
        self.h1_parts = []
        self.title_open = False
        self.h1_open = False
        self.h1_count = 0
        self.metas = []
        self.links = []
        self.image_total = 0
        self.image_empty_alt = 0
        self.jsonld_count = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.title_open = True
        elif tag == "h1":
            self.h1_open = True
            self.h1_count += 1
            self.h1_parts.append([])
        elif tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            self.links.append(a)
        elif tag == "img":
            self.image_total += 1
            if not (a.get("alt") or "").strip():
                self.image_empty_alt += 1
        elif tag == "script" and (a.get("type") or "").lower() == "application/ld+json":
            self.jsonld_count += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_open = False
        elif tag == "h1":
            self.h1_open = False

    def handle_data(self, data):
        if self.title_open:
            self.title_parts.append(data)
        if self.h1_open and self.h1_parts:
            self.h1_parts[-1].append(data)

    def meta_values(self, name):
        name = name.lower()
        return [(tag.get("content") or "").strip() for tag in self.metas
                if (tag.get("name") or tag.get("property") or "").lower() == name]

    def canonicals(self):
        return [(tag.get("href") or "").strip() for tag in self.links
                if "canonical" in (tag.get("rel") or "").lower().split()]

    def to_public_record(self):
        desc = self.meta_values("description")
        robots = self.meta_values("robots")
        og_title = self.meta_values("og:title")
        return {
            "title": " ".join("".join(self.title_parts).split()),
            "h1": [" ".join("".join(chunks).split()) for chunks in self.h1_parts],
            "h1_count": self.h1_count,
            "meta_descriptions": desc,
            "og_titles": og_title,
            "og_descriptions": self.meta_values("og:description"),
            "og_images": self.meta_values("og:image"),
            "canonicals": self.canonicals(),
            "robots": robots,
            "meta_noindex": any("noindex" in r.lower() for r in robots),
            "jsonld_blocks": self.jsonld_count,
            "images_total": self.image_total,
            "images_empty_alt_including_decorative": self.image_empty_alt,
            "flags": (["missing description"] if not any(desc) else [])
                     + (["missing OG title"] if not any(og_title) else [])
                     + (["missing canonical"] if not self.canonicals() else [])
                     + (["missing H1"] if self.h1_count == 0 else [])
                     + (["multiple H1 (review)"] if self.h1_count > 1 else []),
        }


def snapshot(url):
    if not valid_url(url):
        raise ValueError("Only the exact HTTPS alpencrew.com domain is permitted")
    opener = build_opener(NoRedirect)
    req = Request(url, headers={"User-Agent": "AlpenCrewPublicPilot/1.0",
                                "Accept": "text/html"})
    try:
        with opener.open(req, timeout=25) as response:
            if not valid_url(response.geturl()):
                raise ValueError("Unexpected final URL")
            status = response.status
            ctype = response.headers.get("Content-Type", "")
            xrobots = response.headers.get("X-Robots-Tag", "")
            body = response.read(MAX_BYTES + 1)
    except HTTPError as err:
        return {"url": url, "http_status": err.code,
                "redirect_location": err.headers.get("Location", "") if 300 <= err.code < 400 else "",
                "flags": [f"HTTP {err.code} — inspect before any change"]}
    except (TimeoutError, URLError) as err:
        return {"url": url, "http_status": None,
                "flags": [f"connection failure: {type(err).__name__}"]}
    if len(body) > MAX_BYTES:
        return {"url": url, "http_status": status,
                "flags": ["HTML exceeded bounded read size"]}
    if "html" not in ctype.lower():
        return {"url": url, "http_status": status,
                "flags": ["non-HTML response"]}
    parser = Metadata()
    parser.feed(body.decode("utf-8", errors="replace"))
    record = {"url": url, "http_status": status, "x_robots_tag": xrobots}
    record.update(parser.to_public_record())
    if status != 200:
        record["flags"].append(f"HTTP {status}")
    return record


def main():
    arg = argparse.ArgumentParser()
    arg.add_argument("--output-dir", default="seo-baseline-out")
    args = arg.parse_args()
    records = [snapshot(url) for url in PILOT_URLS]
    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    data = {"generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "scope": "public selected URLs only; not Search Console indexing data",
            "wordpress_modified": False, "credentials_used": False,
            "records": records}
    (out / "baseline.json").write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                                         encoding="utf-8")
    rows = ["# Alpen Crew public SEO pilot — BEFORE snapshot", "",
            f"Generated UTC: {data['generated_at_utc']}", "",
            "GET-only. No authenticated REST requests or WordPress writes.", "",
            "| URL | HTTP | H1 count | Meta description | Canonical | OG title |",
            "|---|---:|---:|---|---|---|"]
    for r in records:
        rows.append("| " + " | ".join([
            r["url"], str(r.get("http_status", "-")), str(r.get("h1_count", "-")),
            "yes" if any(r.get("meta_descriptions", [])) else "no",
            "yes" if r.get("canonicals") else "no",
            "yes" if any(r.get("og_titles", [])) else "no",
        ]) + " |")
    (out / "baseline.md").write_text("\n".join(rows) + "\n", encoding="utf-8")
    print("\n".join(rows))
    print("\nNo content updated; output is a public baseline, not a live fix.")


if __name__ == "__main__":
    main()
