#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Query Reddit API and print the first 10 hot post titles."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (ALU-Task/1.0)"}
    params = {"limit": 10}

    try:
        response = requests.get(
            url, headers=headers, params=params,
            allow_redirects=False, timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get("data", {}).get("children", [])
        for post in posts[:10]:
            print(post.get("data", {}).get("title"))
    except Exception:
        print(None)
