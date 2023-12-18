#!/usr/bin/python3
"""Starts a Flask web app"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """ get all employee """
    base_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f'{base_url}/users/{employee_id}')
    users = requests.get(f'{base_url}/todos?userId={employee_id}')

    user_data = user.json()
    users_data = user.json()

    employee_name = user_data['name']
    all_employee = len(users_data)
    tasks = sum(1 for todo in users_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks\
        ({tasks}/{all_employee}):")

    for todo in users_data:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
