#!/usr/bin/python3
"""Module to gather employee to do information from an API"""
import csv
import requests
import sys


def employee_todo_to_csv():
    """This method gathers employee to do information from an API
    Employee task information is sent to a CSV file
    """
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    employee_name = requests.get(url + 'users/{}'.format(employee_id))
    employee_todo = requests.get(url + 'todos?userId={}'.format(employee_id))

    employee_name = employee_name.json()
    employee_todo = employee_todo.json()

    with open('{}.csv'.format(employee_id), 'w', encoding='UTF8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in employee_todo:
            data = [employee_id, employee_name.get("username"),
                    task.get("completed"), task.get("title")]
            writer.writerow(data)

if __name__ == "__main__":
    employee_todo_to_csv()
