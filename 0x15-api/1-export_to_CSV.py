#!/usr/bin/python3
'''script to export data in the CSV format'''
import csv
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(argv[1])).json()

    with open("{}.csv".format(argv[1]), "w", newline="") as csv_file:
        tasks = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos:
            tasks.writerow([argv[1], user.get("username"),
                            task.get("completed"), task.get("title")])
