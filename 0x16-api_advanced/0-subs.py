#!/usr/bin/python3
""" Python scipt that query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        return dataa.get("subscribers", 0)
    elif response.status_code == 404:
        return 0
    else:
        return 0

    # results = response.json().get("data")
    # return results.get("subscribers")
