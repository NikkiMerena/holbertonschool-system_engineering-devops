#!/usr/bin/python3

"""
This module fetches information about an employee's TODO list progress based on the given employee ID.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches information about an employee's TODO list progress based on the given employee ID.
    """
    # Fetching the employee's details
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_details = response.json()

    # Fetching the employee's todo list
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_list = response.json()

    # Calculating the employee's todo progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task.get("completed"))

    # Displaying the progress report
    employee_name = employee_details.get("name", "Unknown Employee")
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task in todo_list:
        if task.get("completed"):
            print(f"\t- {task['title']}")


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
