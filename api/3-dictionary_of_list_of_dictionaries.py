#!/usr/bin/python3
"""This is the importation of the modules"""
import json
import requests

if __name__ == ('__main__'):
    """this function record all the tasks from all employees"""
    # Get the list of all users
    url_users = "https://jsonplaceholder.typicode.com/users"
    response_users = requests.get(url_users)
    users = response_users.json()

    # Create an empty dictionary to store all the tasks
    all_tasks = {}

    # Loop through all users and fetch their tasks
    for user in users:
        user_id = user["id"]
        username = user["username"]
        i = user_id

        # Fetch the TODO list for the user
        url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={i}"
        response_todos = requests.get(url_todos)
        todos = response_todos.json()

        # Create a list to store the tasks of the current user
        user_tasks = []

        # Loop through all tasks of the current user and append to the list
        for todo in todos:
            task = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            user_tasks.append(task)

        # Add the list of tasks of the current user to the all_tasks dictionary
        all_tasks[user_id] = user_tasks

    # Save the data in the desired JSON format to a file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)
