#!/usr/bin/python3
"""Recursively return a list of all hot article titles for a subreddit."""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return list of all hot post titles for a subreddit (recursively)."""
    if hot_list is None:
        hot_list = []
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-Reddit-Task/1.0"}
    params = {"after": after, "limit": 100}
    try:
        r = requests.get(url, headers=headers,
                         params=params, allow_redirects=False, timeout=10)
        if r.status_code != 200:
            return None
        data = r.json().get("data", {})
        children = data.get("children", [])
        if not children:
            return hot_list
        for post in children:
            hot_list.append(post.get("data", {}).get("title"))
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    except requests.RequestException:
        return None
