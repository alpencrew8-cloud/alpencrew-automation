#!/usr/bin/env python3
"""Read-only inventory of WordPress editing capabilities. Never print credentials or private records."""
import base64
import json
import os
import urllib.error
import urllib.parse
import urllib.request

ROOT="https://alpencrew.com"

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None

opener=urllib.request.build_opener(NoRedirect)

def read(path, username, password):
    target=ROOT+path
    auth=base64.b64encode((username+":"+password).encode("utf-8")).decode("ascii")
    request=urllib.request.Request(target, headers={
        "Authorization":"Basic "+auth,
        "Accept":"application/json",
        "User-Agent":"AlpenCrewReadOnlyCapabilities/1.0"
    }, method="GET")
    try:
        with opener.open(request, timeout=20) as response:
            destination=urllib.parse.urlparse(response.url)
            if destination.scheme!="https" or destination.hostname!="alpencrew.com":
                raise ValueError("Unrecognized redirect")
            raw=response.read(1500000)
            return response.status,json.loads(raw)
    except urllib.error.HTTPError as e:
        return e.code,None
    except (urllib.error.URLError, TimeoutError, ValueError, json.JSONDecodeError):
        return "connection error",None

def main():
    username=os.environ.get("WP_USERNAME","").strip()
    password=os.environ.get("WP_APPLICATION_PASSWORD","").strip()
    if not username or not password:
        print("Not configured: missing environment credentials.")
        raise SystemExit(2)
    tests=[
        ("WordPress pages (editable context)","/wp-json/wp/v2/pages?context=edit&per_page=1"),
        ("WordPress posts (editable context)","/wp-json/wp/v2/posts?context=edit&per_page=1"),
        ("WordPress media (editable context)","/wp-json/wp/v2/media?context=edit&per_page=1"),
        ("WordPress post types","/wp-json/wp/v2/types?context=edit"),
        ("WordPress plugin inventory","/wp-json/wp/v2/plugins?per_page=100"),
        ("WordPress active theme","/wp-json/wp/v2/themes?status=active"),
        ("WooCommerce products endpoint","/wp-json/wc/v3/products?per_page=1"),
    ]
    print("# Alpen Crew - Authenticated, Read-only API Capability Audit")
    print("No private data or passwords are printed; no site content is modified.")
    print("")
    for label,path in tests:
        status,data=read(path,username,password)
        print(f"- {label}: HTTP {status}" if isinstance(status,int) else f"- {label}: {status}")
        if label=="WordPress post types" and status==200 and isinstance(data,dict):
            exposed=set(data.keys())
            for typ in ["page","post","product","product_cat","elementor_library","woodmart_slide","woodmart_sidebar"]:
                print(f"  - REST type {typ} exposed: {'yes' if typ in exposed else 'no'}")
        if label=="WordPress plugin inventory" and status==200 and isinstance(data,list):
            installed=[str(p.get("plugin","")).lower() for p in data if isinstance(p,dict)]
            families={
                "WooCommerce":("woocommerce/",),
                "Elementor":("elementor/","elementor-pro/"),
                "Yoast SEO":("wordpress-seo/",),
                "Rank Math":("seo-by-rank-math/",),
                "All in One SEO":("all-in-one-seo-pack/","all-in-one-seo/"),
                "SEOPress":("wp-seopress/",),
                "Smash Balloon Instagram":("instagram-feed/","instagram-feed-pro/"),
                "LiteSpeed Cache":("litespeed-cache/",),
                "JetBackup":("backup/","jetbackup/")
            }
            for family,prefixes in families.items():
                found=any(slug.startswith(prefix) for slug in installed for prefix in prefixes)
                print(f"  - {family} detected: {'yes' if found else 'no'}")
    print("")
    print("Reminder: HTTP 200 on a read endpoint does not prove write permissions or SEO field mutability.")
    print("No live editing workflows are enabled.")

if __name__=="__main__":
    main()
