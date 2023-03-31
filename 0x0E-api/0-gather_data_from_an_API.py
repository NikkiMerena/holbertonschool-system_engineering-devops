#!/usr/bin/python3

"""
This module fetches information about an employee's TODO list progress based on the given employee ID.
"""

import requests
import sys


def get_todo_progress(employee_id):
    """
    Fetches information about an employee's TODO list progress based on the given employee ID.
    """
    # Fetching the employee's details
    url_employee = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url_employee)
    employee_details = response.json()

    # Fetching the employee's todo list
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(url_todos)
    todo_list = response.json()

    # Calculating the employee's todo progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task.get("completed"))

    # Displaying the progress report
    employee_name = employee_details.get("name", "Unknown Employee")
    progress_msg = f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):"
    print(progress_msg)
    for task in todo_list:
        if task.get("completed"):
            task_title = f"\t- {task['title']}"
            print(task_title)


if __name__ == "__main__":
    employee_id = sys.argv[1]
    get_todo_progress(employee_id)
