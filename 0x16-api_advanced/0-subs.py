#!/usr/bin/python3
"""
Python script that queries subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        print(f"The subreddit r/{subreddit} does not exist.")
        return 0
    else:
        print(f"Failed to retrieve data for subreddit r/{subreddit}. Status code: {response.status_code}")
        return -1
