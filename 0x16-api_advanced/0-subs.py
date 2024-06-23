#!/usr/bin/python3
''' 
Python script that gather and display employee data using REST API
'''
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        base_url = "https://jsonplaceholder.typicode.com/"
        
        user_response = requests.get(f"{base_url}users/{user_id}")
        user_name = user_response.json().get("name")
        
        if user_name:
            tasks_response = requests.get(f"{base_url}todos?userId={user_id}")
            tasks = tasks_response.json()
            completed_tasks = [task for task in tasks if task.get("completed")]
            
            print(f"Employee {user_name} is done with tasks({len(completed_tasks)}/{len(tasks)}):")
            for task in completed_tasks:
                print(f"\t {task.get('title')}")
