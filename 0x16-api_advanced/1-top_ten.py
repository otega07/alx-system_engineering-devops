#!/usr/bin/python3
"""
This module contains the function top_ten
"""
import requests
from sys import argv


def top_ten(subreddit):
    """
    Returns the top ten hot posts for a given subreddit
    """
    user = {'User-Agent': 'python:top_ten:v1.0 (by /u/yourusername)'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=user, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json().get('data')
        for post in data.get('children'):
            print(post.get('data').get('title'))
    except Exception:
        print(None)


if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
