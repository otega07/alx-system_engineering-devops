#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        results = response.json().get("data")
        children = results.get("children")
        if not children:
            print("None")
        else:
            for post in children:
                print(post.get("data").get("title"))
    except (requests.exceptions.JSONDecodeError, AttributeError):
        print("None")


if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ").strip()
    top_ten(subreddit)
