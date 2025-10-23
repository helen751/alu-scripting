#!/usr/bin/python3
"""Return number of subscribers for a given subreddit using Reddit API."""

import requests


def number_of_subscribers(subreddit):
    """Return total subscribers for a subreddit, or 0 if invalid."""
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "ALU-Reddit-Task/1.0"}
    try:
        r = requests.get(url, headers=headers,
                         allow_redirects=False, timeout=10)
        if r.status_code != 200:
            return 0
        data = r.json().get("data", {})
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0
