#!/usr/bin/python3
"""this is the API requestes and the handling of the data"""


import requests
import sys


if __name__ == '__main__':
    """This is the requests of the api and the usage of it"""
    id = sys.argv[1]

    # Fetch the employee data
    str = 'https://jsonplaceholder.typicode.com/users/'
    response = requests.get(f"{str}{id}")
    e_data = response.json()

    # Fetch the TODO list for the employee
    strus = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(f"{strus}")
    todo_list = response.json()

    # Count the number of completed tasks
    completed_tasks = []
    tasks = 0
    for i in todo_list:
        if i['userId'] == int(id):
            tasks += 1
            if i['completed'] == 1:
                completed_tasks.append(i)
    n_tasks = len(completed_tasks)

    # Print the TODO list progress
    d = " is done with tasks("
    print(f"Employee {e_data['name']}{d}{n_tasks}/{tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}\n")
