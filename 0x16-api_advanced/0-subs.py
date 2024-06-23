#!/usr/bin/python3
''' 
Python function that queries the Reddit API and returns the number of subscribers
'''

import requests

def all_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Reddit Bot by /u/AgitatedVegetable247'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == "__main__":
    subreddit = "Kome"
    subscribers = all_subscribers(subreddit)
    print(f"The number of subscribers in r/{subreddit} is: {subscribers}")
