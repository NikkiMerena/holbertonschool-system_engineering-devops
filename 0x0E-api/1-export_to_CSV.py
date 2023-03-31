#!/usr/bin/python3
"""Module to gather employee to do information from an API"""
import csv
import requests
import sys


def get_employee_todo():
    """This method gathers employee to do information from an API
    See README for display format
    """
    num_complete = 0
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    employee_name = requests.get(url + 'users/{}'.format(employee_id))
    employee_todo = requests.get(url + 'todos?userId={}'.format(employee_id))

    employee_name = employee_name.json()
    employee_todo = employee_todo.json()

    # print("employee name response", end="")
    # print(employee_name)
    # print("todo response", end="")
    # print(employee_todo)

    completed = []

    for task in employee_todo:
        if task.get("completed") is True:
            num_complete += 1
            completed.append(task)

    name = employee_name.get("name")
    a = num_complete
    b = len(employee_todo)
    print("Employee {} is done with tasks({}/{}):".format(name, a, b))

    # Export to CSV
    with open(f"{employee_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in completed:
            writer.writerow([employee_id, name,
                            task.get("completed"), task.get("title")])


if __name__ == "__main__":
    get_employee_todo()
