#!/usr/bin/python3
'''
Python script that queries the Reddit API for the number of subscribers for a subreddit.
'''

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' does not exist.")
        return 0
    else:
        print(f"Error fetching data for subreddit '{subreddit}': {response.status_code}")
        return 0

if __name__ == "__main__":
    subreddit = input("Enter a subreddit name: ").strip()
    subscribers = number_of_subscribers(subreddit)
    print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
