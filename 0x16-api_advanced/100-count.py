#!/usr/bin/python3
"""Script to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Print counts of given words found in hot posts of a given subreddit.
    
    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        instances (dict): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    try:
        if response.status_code == 404:
            raise Exception
        results = response.json()
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")

    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        for word in word_list:
            word_lower = word.lower()
            if word_lower in title:
                times = len([t for t in title if t == word_lower])
                if instances.get(word_lower) is None:
                    instances[word_lower] = times
                else:
                    instances[word_lower] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        for k, v in instances:
            print("{}: {}".format(k, v))
    else:
        count_words(subreddit, word_list, instances, after, count)


if __name__ == "__main__":
    # Example usage
    subreddit = input("Enter a subreddit: ").strip()
    words = input("Enter words to count (comma-separated): ").strip().split(",")
    words = [word.strip() for word in words]
    count_words(subreddit, words)
