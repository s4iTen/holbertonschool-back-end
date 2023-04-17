#!/usr/bin/python3
"""this is the API requestes and the handling of the data"""

import json
import sys
from urllib import request

if __name__ == '__main__':
    """This is the requests of the api and the usage of it"""
    employee_id = sys.argv[1]

    # Fetch the employee data
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    with request.urlopen(url) as f:
        e_data = json.loads(f.read())

    # Fetch the TODO list for the employee
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    with request.urlopen(url) as f:
        todo_list = json.loads(f.read())

    # Count the number of completed tasks
    completed_tasks = [task for task in todo_list if task["completed"] == True]
    n_tasks = len(completed_tasks)

    # Print the TODO list progress
    d = " is done with tasks("
    print(f"Employee {e_data['name']}{d}{n_tasks}/{len(todo_list)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
