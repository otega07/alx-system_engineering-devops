#!/usr/bin/python3
'''
Python script that gather and display employee task data from API
'''

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1 and argv[1].isdigit():
        user_id = int(argv[1])
        base_url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(f"{base_url}users/{user_id}")
        user_data = user_response.json()
        user_name = user_data.get("name")
        if user_name:
            tasks_response = requests.get(f"{base_url}todos?userId={user_id}")
            tasks_data = tasks_response.json()
            completed_tasks = [task for task in tasks_data if task.get("completed")]
            total_tasks = len(tasks_data)
            completed_count = len(completed_tasks)
            print(f"Employee {user_name} is done with tasks({completed_count}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
