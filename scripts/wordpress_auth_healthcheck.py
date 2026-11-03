#!/usr/bin/env python3
"""Alpen Crew WordPress authenticated API connectivity check.

Does NOT change content. Designed for a future owner-approved GitHub Actions
environment. Never print credentials or Authorization headers.
Requires WP_USERNAME and WP_APPLICATION_PASSWORD environment variables.
"""
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

SITE = "https://alpencrew.com"
ENDPOINT = SITE + "/wp-json/wp/v2/users/me?context=edit"


def main():
    username = os.environ.get("WP_USERNAME", "").strip()
    password = os.environ.get("WP_APPLICATION_PASSWORD", "").strip()
    if not username or not password:
        print("NOT_CONFIGURED: Missing GitHub environment secrets. No request made.")
        return 2

    class NoRedirect(urllib.request.HTTPRedirectHandler):
        # Never forward an Authorization header to a redirected destination.
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = urllib.request.build_opener(NoRedirect)
    auth = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("ascii")
    request = urllib.request.Request(
        ENDPOINT,
        headers={
            "Authorization": "Basic " + auth,
            "Accept": "application/json",
            "User-Agent": "AlpenCrewWPConnectionTest/1.0",
        },
    )
    try:
        with opener.open(request, timeout=20) as response:
            target = urllib.parse.urlparse(response.url)
            if target.scheme != "https" or target.hostname != "alpencrew.com":
                print("FAIL: Unexpected redirect target. Review the website configuration.")
                return 1
            code = response.status
            body = response.read(10_000)
            try:
                obj = json.loads(body)
            except json.JSONDecodeError:
                obj = {}
            if code == 200 and isinstance(obj, dict) and isinstance(obj.get("id"), int):
                print("SUCCESS: Authenticated WordPress REST API user endpoint responds correctly.")
                print("No WordPress content was modified.")
                return 0
            print("FAIL: Unexpected authenticated API response.")
            return 1
    except urllib.error.HTTPError as exc:
        print(f"FAIL: WordPress returned HTTP {exc.code}. Check account permissions and server Authorization forwarding.")
        return 1
    except urllib.error.URLError:
        print("FAIL: Connection or TLS error. Check website connectivity.")
        return 1
    except TimeoutError:
        print("FAIL: WordPress request timed out.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
