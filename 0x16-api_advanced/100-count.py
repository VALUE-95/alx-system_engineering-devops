#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Recursively queries the Reddit API, parses the title of hot
    articles, and prints a sorted count of given keywords.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count occurrences for.
        after (str, optional): A token indicating the starting point
        for the next page of results. Defaults to None.
        counts (dict, optional): A dictionary to store the counts of
        keywords. Defaults to None.
    """
    if counts is None:
        counts = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    params = {"limit": 100}  # Retrieve up to 100 posts per request

    if after:
        params["after"] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()["data"]
        posts = data["children"]
        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(
                        word.lower(), 0) + title.count(word.lower())

        # Check if there are more pages of results
        after = data.get("after")
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        print(None)
