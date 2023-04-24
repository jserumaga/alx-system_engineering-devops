#!/usr/bin/python3
"""extend your Python script to export data in the JSON format
"""
import json
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    name_user = user['name']
    todos = requests.get(url + "users/{}/todos".format(argv[1])).json()

    with open("{}.json".format(argv[1]), "w") as jsonfile:
        json.dump({argv[1]: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": name_user
            } for t in todos]}, jsonfile)
