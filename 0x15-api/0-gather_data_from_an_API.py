#!/usr/bin/python3
'''
Returns information about his/her list progress.
'''
import requests
from sys import argv
if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "users/{}/todos".format(argv[1])).json()
    name_user = user['name']
    task_completed = 0
    total_task = 0

    for task in todos:
        total_task += 1
        if task.get('completed'):
            task_completed += 1
    print('Employee {} is done with tasks({:d}/{:d}):'
          .format(name_user, task_completed, total_task))

    for task in todos:
        if task.get('completed'):
            print('\t {}'.format(task['title']))
