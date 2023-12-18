#!/usr/bin/python3
"""Starts a Flask web app"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ get all employee """

    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{base_url}/users/{employee_id}')
    todos = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user.json()
    todos_data = todos.json()

    employee_name = user_data['name']
    all_employee = len(todos_data)
    tasks = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks\
           ({tasks}/{all_employee}):")

    for todo in todos_data:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
