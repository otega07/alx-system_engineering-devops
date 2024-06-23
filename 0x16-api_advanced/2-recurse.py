#!/usr/bin/python3
"""
Python script that queries a list of all hot posts on a given Reddit subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        
        for child in data.get("children"):
            hot_list.append(child.get("data").get("title"))
        
        if after:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    subreddit = input("Enter a subreddit: ").strip()
    hot_posts = recurse(subreddit)
    
    if hot_posts is None:
        print(f"Subreddit '{subreddit}' not found or invalid.")
    else:
        print(f"List of hot posts in r/{subreddit}:")
        for idx, post in enumerate(hot_posts, start=1):
            print(f"{idx}. {post}")
