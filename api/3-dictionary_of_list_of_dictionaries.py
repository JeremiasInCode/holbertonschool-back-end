#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import requests

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def user_info():
    """ Check user info """
    
    with open('todo_all_employees.json', 'r') as f:
        student_json = json.load(f)

    correct_json = requests.get(users_url).json()

    for correct_entry in correct_json:
        if correct_entry['id'] not in student_json:
            print("User ID {} Found: Incorrect".format(correct_entry['id']))
            return
    
    print("All users found: OK")


def get_employee_todo_progress(employee, base_url):
    """ Get employee todo"""

    all_response = requests.get(f'{base_url}/todos?userId={employee["id"]}')
    all_data = all_response.json()
    employee_name = employee['username']

    lis_data = []
    for todo in all_data:
        dic_data = {"username": employee_name,
                    "task": todo["title"],
                    "completed": todo["completed"]}
        lis_data.append(dic_data)

    return lis_data


if __name__ == '__main__':
    base_url = 'https://jsonplaceholder.typicode.com'
    user_response = requests.get(f'{base_url}/users/')
    user_data = user_response.json()

    json_form = {}
    for employee in user_data:
        key = employee['id']
        json_form[key] = get_employee_todo_progress(employee, base_url)

    with open("todo_all_employees.json", 'w') as f:
        json.dump(json_form, f)

    # Check user info
    user_info()
