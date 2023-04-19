#!/usr/bin/python3
'''this is the importation of the modules'''
import sys
import json
import requests

if __name__ == ('__main__'):
    """this function export the data as json file"""
    # Set the employee id
    id = sys.argv[1]

    # Fetch the employee data
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    response = requests.get(url)
    d = response.json()

    # Fetch the TODO list for the employee
    url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
    response = requests.get(url)
    todo_list = response.json()

    # Create a dictionary with the required format
    data = {str(id): []}
    u = 'username'
    c = 'completed'
    for t in todo_list:
        data[str(id)].append({"task": t["title"], c: t[c], "username": d[u]})

    # Save the data in a JSON file
    with open(f"{d['id']}.json", "w") as f:
        json.dump(data, f)
