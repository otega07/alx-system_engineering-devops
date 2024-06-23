#!/usr/bin/python3
"""
Python script that gathers and display employee task data from API
"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        url = "https://jsonplaceholder.typicode.com/"
        
        user_response = requests.get(f"{url}users/{user_id}")
        if user_response.status_code == 200:
            user = user_response.json()
            name = user.get("name")
            if name:
                tasks_response = requests.get(f"{url}todos?userId={user_id}")
                tasks = tasks_response.json()
                completed_tasks = [task for task in tasks if task.get("completed")]
                print(f"Employee {name} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
                for task in completed_tasks:
                    print(f"\t {task.get('title')}")
        else:
            print("User not found")
