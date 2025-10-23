#!/usr/bin/python3
"""Print titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Print the top 10 hot post titles for a subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "ALU-Reddit-Task/0.1"}
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
        for post in posts:
            title = post.get("data", {}).get("title")
            print(title)
    except Exception:
        print(None)
