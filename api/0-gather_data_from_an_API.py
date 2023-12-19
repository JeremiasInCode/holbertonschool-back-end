#!/usr/bin/python3
"""Returns information about his/her TODO list progress using requests."""

import json
import sys
import requests


def get_employee_todo_progress(employee_id):
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    user_response = requests.get(api_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Error fetching data.")
        return

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get("name")
    completed_tasks = [task for task in todo_data if task.get("completed")]
    total_tasks = len(todo_data)

    output = [
        f"Employee {employee_name} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}): "
    ]

    for task in completed_tasks:
        output.append(f"\t {task['title']}")

    return "\n".join(output)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        result = get_employee_todo_progress(employee_id)
        print(result)
