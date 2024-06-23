#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""


import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print("None")
        return
    try:
        results = response.json().get("data")
        children = results.get("children")
        if not children:
            print("None")
        else:
            for post in children:
                print(post.get("data").get("title"))
    except ValueError:
        print("None")


if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ").strip()
    top_ten(subreddit)
