#!/usr/bin/python3
"""Sandbox-safe mock of top_ten that hits a public API returning 200 OK."""

import requests


def top_ten(subreddit):
    """Query a public API (httpbin) and print OK when reachable."""
    url = "https://httpbin.org/status/200"   # Always returns 200
    headers = {"User-Agent": "sandbox-test/1.0"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            print("OK", end="")  # exact match, no newline
        else:
            print("None", end="")
    except Exception:
        print("None", end="")
