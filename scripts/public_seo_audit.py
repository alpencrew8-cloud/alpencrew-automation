#!/usr/bin/env python3
"""Read-only, sitemap-wide public SEO audit for alpencrew.com. Standard library only.

No credentials, WordPress writes, paid APIs, or changes to site content.
"""
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
import os
import time
import xml.etree.ElementTree as ET

SITE = "https://alpencrew.com"
ALLOWED_HOSTS = {"alpencrew.com", "www.alpencrew.com"}
MAX_PAGES = 260
USER_AGENT = "AlpenCrewPublicSEOAudit/1.0"


def fetch(url):
    parts = urlparse(url)
    if parts.scheme != "https" or parts.hostname not in ALLOWED_HOSTS:
        raise ValueError("URL is outside the audit scope")
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=20) as response:
            target = urlparse(response.url)
            if target.scheme != "https" or target.hostname not in ALLOWED_HOSTS:
                raise ValueError("Unsafe redirect target")
            return response.status, response.headers.get("Content-Type", ""), response.read(2_000_000)
    except HTTPError as exc:
        return exc.code, "", b""


def localname(element):
    return element.tag.split("}")[-1]


def get_sitemap_urls():
    """Read WordPress XML sitemaps, without visiting more than 20 sitemap files."""
    candidates = [
        SITE + "/wp-sitemap.xml",
        SITE + "/sitemap_index.xml",
        SITE + "/sitemap.xml",
    ]
    for start in candidates:
        queue = [start]
        visited = set()
        urls = []
        while queue and len(visited) < 20:
            url = queue.pop(0)
            if url in visited:
                continue
            visited.add(url)
            try:
                code, _, contents = fetch(url)
                if code != 200:
                    continue
                root = ET.fromstring(contents)
                locs = [(node.text or "").strip() for node in root.iter()
                        if localname(node) == "loc" and node.text]
                if localname(root) == "sitemapindex":
                    queue.extend(u for u in locs
                                 if urlparse(u).hostname in ALLOWED_HOSTS)
                elif localname(root) == "urlset":
                    urls.extend(u for u in locs
                                if urlparse(u).hostname in ALLOWED_HOSTS)
            except (ValueError, URLError, TimeoutError, ET.ParseError):
                pass
        if urls:
            return list(dict.fromkeys(urls)), len(visited)
    return [], 0


class PageTags(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.h1_count = 0
        self.meta = {}
        self.canonicals = 0
        self.schema_blocks = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            name = (attrs.get("name") or attrs.get("property") or "").lower()
            if name:
                self.meta[name] = attrs.get("content", "")
        if tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonicals += 1
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self.schema_blocks += 1

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False

    def handle_data(self, content):
        if self.in_title:
            self.title += content


def priority(url):
    path = urlparse(url).path
    if "/product/" in path:
        return (0, path)
    if "/product-category/" in path:
        return (1, path)
    return (2, path)


def main():
    results = []
    totals = Counter()
    for label, path in [("WordPress public API", "/wp-json/"),
                        ("Robots file", "/robots.txt")]:
        try:
            status, _, _ = fetch(SITE + path)
            results.append(f"- {label}: HTTP {status}")
        except (ValueError, URLError, TimeoutError) as exc:
            results.append(f"- {label}: {type(exc).__name__}")
    urls, sitemap_files = get_sitemap_urls()
    results += [f"- Public XML sitemap entries: {len(urls)}",
                f"- XML sitemap files visited: {sitemap_files}"]
    sample_urls = [SITE + "/"] + [
        u for u in sorted(urls, key=priority) if u.rstrip("/") != SITE
    ][: MAX_PAGES - 1]
    detail = []
    titles = {}
    meta_descriptions = {}
    types = Counter()
    for pos, url in enumerate(sample_urls):
        path = urlparse(url).path
        category = ("product" if "/product/" in path else
                    "product category" if "/product-category/" in path else
                    "blog / archive" if "/category/" in path or "/tag/" in path else
                    "other page")
        types[category] += 1
        try:
            status, content_type, body = fetch(url)
            issues = []
            if status != 200:
                issues.append(f"HTTP {status}")
            elif "html" not in content_type.lower():
                issues.append("Non-HTML response")
            else:
                tags = PageTags()
                tags.feed(body.decode("utf-8", "replace"))
                title = tags.title.strip()
                desc = tags.meta.get("description", "").strip()
                if not title:
                    issues.append("missing title")
                else:
                    titles.setdefault(title.casefold(), []).append(url)
                if desc:
                    meta_descriptions.setdefault(desc.casefold(), []).append(url)
                if len(title) > 65:
                    issues.append("title over 65 characters (review)")
                if len(desc) > 165:
                    issues.append("meta description over 165 characters (review)")
                if not tags.meta.get("description", "").strip():
                    issues.append("missing meta description")
                if not tags.canonicals:
                    issues.append("missing canonical")
                if tags.h1_count == 0:
                    issues.append("missing H1")
                if tags.h1_count > 1:
                    issues.append("multiple H1")
                if not tags.meta.get("og:title"):
                    issues.append("missing OG title")
                if tags.schema_blocks == 0:
                    issues.append("no JSON-LD observed")
                if "noindex" in tags.meta.get("robots", "").lower():
                    issues.append("meta noindex present")
            for issue in issues:
                totals[issue] += 1
            detail.append((url, issues))
        except (ValueError, URLError, TimeoutError) as exc:
            totals["connection error"] += 1
            detail.append((url, [type(exc).__name__]))
        if pos < len(sample_urls) - 1:
            time.sleep(0.25)

    duplicate_titles = {k: v for k, v in titles.items() if len(v) > 1}
    duplicate_descriptions = {k: v for k, v in meta_descriptions.items() if len(v) > 1}
    totals["duplicate titles (URLs affected)"] = sum(len(v) for v in duplicate_titles.values())
    totals["duplicate meta descriptions (URLs affected)"] = sum(len(v) for v in duplicate_descriptions.values())
    report = [
        "# Alpen Crew — Public, Read-only SEO Audit",
        f"Generated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M UTC}",
        "",
        "No API credentials used. No WordPress changes performed.",
        "Results cover public URLs discovered in XML sitemaps, not necessarily all live URLs, indexing, rankings, or traffic.",
        "",
        "## Connectivity and scope", *results,
        f"- URLs checked: {len(sample_urls)}", "",
        "## URLs by type",
        *[f"- {kind}: {count}" for kind, count in sorted(types.items())],
        "",
        "## Observations", "| Check | Sample count |", "|---|---:|",
    ]
    report.extend(f"| {key} | {value} |" for key, value in sorted(totals.items()))
    report.extend(["", "## Duplicate page titles (groups)", ""])
    if duplicate_titles:
        for _, matches in list(duplicate_titles.items())[:20]:
            report.extend(["- " + " | ".join(matches)])
    else:
        report.append("- No duplicate titles found in inspected pages")
    report.extend(["", "## Pages inspected", "| URL | Findings |", "|---|---|"])
    for url, issues in detail:
        report.append(f"| {url} | {', '.join(issues) if issues else 'No sampled flags'} |")
    report.extend(["", "Interpretation: manually validate before implementing SEO changes. This includes only sitemap-discoverable URLs; a browser render and Search Console can reveal more."])
    text = "\n".join(report) + "\n"
    print(text)
    summary = os.getenv("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as output:
            output.write(text)


if __name__ == "__main__":
    main()
