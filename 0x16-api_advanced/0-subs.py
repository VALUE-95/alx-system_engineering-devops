#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers
for a given subreddit using PRAW.
"""

import praw


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit using PRAW.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit.
        If the subreddit is invalid, returns 0.
    """
    reddit = praw.Reddit(user_agent="Subreddit Subscriber Count Bot")
    try:
        sub = reddit.subreddit(subreddit)
        return sub.subscribers
    except Exception as e:
        print(f"Error: {e}")
        return 0
