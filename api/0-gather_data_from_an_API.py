#!/usr/bin/python3
"""Returns information about his/her TODO list progress using urllib."""

import requests
from sys import argv


if __name__ == '__main__':
    """
        Main Function of the program.
    """

    api_url = f'https://jsonplaceholder.typicode.com/'

    user_id = int(argv[1])
    user_data = requests.get(api_url + f'users/{user_id}').json()
    user_tasks = requests.get(api_url + f'users/{user_id}/todos').json()

    user_completed_tasks = [i for i in user_tasks if i['completed']]

    print(f'Employee {user_data["name"]} is done with ', end='')
    print(f'tasks({len(user_completed_tasks)}/{len(user_tasks)}):')

    for task in user_completed_tasks:
        print("\t " + task["title"])
