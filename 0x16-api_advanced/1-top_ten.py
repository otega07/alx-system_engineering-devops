#!/python3
"""
This module contains the function top_ten.
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    headers = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get('data')
        children = data.get('children')
        if not children:
            print(None)
            return
        for post in children:
            print(post.get('data').get('title'))
    except (KeyError, TypeError, ValueError):
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
