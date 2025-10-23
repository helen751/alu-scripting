#!/usr/bin/python3
"""Recursively count given keywords in hot article titles of a subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Count occurrences of words in hot post titles (recursive)."""
    if counts is None:
        counts = {}
        # merge duplicates case-insensitively
        temp = {}
        for w in word_list:
            lw = w.lower()
            temp[lw] = temp.get(lw, 0) + 1
        word_list = list(temp.keys())
        counts = {w: 0 for w in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALU-Reddit-Task/1.0"}
    params = {"after": after, "limit": 100}
    try:
        r = requests.get(url, headers=headers,
                         params=params, allow_redirects=False, timeout=10)
        if r.status_code != 200:
            return
        data = r.json().get("data", {})
        children = data.get("children", [])
        for post in children:
            title = post.get("data", {}).get("title", "").lower().split()
            for word in counts.keys():
                counts[word] += title.count(word)
        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)

        # sort and print results
        sorted_counts = sorted(
            [(w, c) for w, c in counts.items() if c > 0],
            key=lambda kv: (-kv[1], kv[0])
        )
        for w, c in sorted_counts:
            print(f"{w}: {c}")
    except requests.RequestException:
        return
