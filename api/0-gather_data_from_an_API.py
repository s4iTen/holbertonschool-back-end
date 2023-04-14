#!/usr/bin/python3
"""this is the API requestes and the handling of the data"""


import requests
import sys


if __name__ == '__main__':
    """This is the requests of the api and the usage of it"""
    employee_id = sys.argv[1]

    # Fetch the employee data
    str = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(f"{str}{employee_id}")
    e_data = response.json()

    # Fetch the TODO list for the employee
    strus = 'https://jsonplaceholder.typicode.com/todos?userId='
    response = requests.get(f"{strus}{employee_id}")
    todo_list = response.json()

    # Count the number of completed tasks
    completed_tasks = [task for task in todo_list if task["completed"]]
    n_tasks = len(completed_tasks)

    # Print the TODO list progress
    d = " is done with tasks("
    print(f"Employee {e_data['name']}{d}{n_tasks}/{len(todo_list)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")
