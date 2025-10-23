#!/usr/bin/python3
"""Print the titles of the first 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    if subreddit is None or not isinstance(subreddit, str):
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
            # invalid subreddit → print nothing
            return

        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children:
            # no posts → print nothing
            return

        for post in children:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        # if any error → print nothing
        return
