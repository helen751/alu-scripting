#!/usr/bin/python3
"""Print titles of first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Print the top 10 hot post titles for a subreddit."""
    if subreddit is None or type(subreddit) is not str:
        print(None)
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "ALU-Reddit-Task/1.0"}
    try:
        r = requests.get(url, headers=headers,
                         allow_redirects=False, timeout=10)
        if r.status_code != 200:
            print(None)
            return
        posts = r.json().get("data", {}).get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    except requests.RequestException:
        print(None)
