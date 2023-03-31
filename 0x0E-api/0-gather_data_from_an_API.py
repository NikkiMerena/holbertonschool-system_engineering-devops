#!/usr/bin/python3
"""Module to gather employee to do information from an API"""
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
            completed.append(task.get("title"))
    # print(num_complete)
    # print(len(employee_todo))
    name = employee_name.get("name")
    a = num_complete
    b = len(employee_todo)
    print("Employee {} is done with tasks({}/{}):".format(name, a, b))
    for task in completed:
        print("\t {}".format(task))


if __name__ == "__main__":
    get_employee_todo()
