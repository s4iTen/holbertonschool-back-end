#!/usr/bin/python3
"""this """
import csv
import requests
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} id")
    sys.exit(1)

id = sys.argv[1]

# Fetch the employee data
url = f"https://jsonplaceholder.typicode.com/users/{id}"
response = requests.get(url)
e_data = response.json()

# Fetch the TODO list for the employee
url = f"https://jsonplaceholder.typicode.com/todos?userId={id}"
response = requests.get(url)
todo_list = response.json()

# Write the data to a CSV file
filename = f"{id}.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    for t in todo_list:
        writer.writerow([id, e_data['username'], t['completed'], t['title']])
