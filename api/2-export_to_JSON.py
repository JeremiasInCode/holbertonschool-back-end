#!/usr/bin/python3
"""Starts a Flask web app"""

import json
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ get all employee """

    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{base_url}/users/{employee_id}')
    todos = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user.json()
    todos_data = todos.json()

    employee_name = user_data['username']

    data = []
    for element in todos_data:
        json_data = {
            "task": element["title"],
            "completed": element["completed"],
            "username": employee_name
        }
        data.append(json_data)

    filename = f'{employee_id}.json'

    with open(filename, 'w') as f:
        json.dump({f"{employee_id}": data}, f)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
