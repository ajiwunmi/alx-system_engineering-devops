#!/usr/bin/python3
import sys
import requests
import csv
import json

print("This is the name of the script:", sys.argv[0])
print("Number of arguments:", len(sys.argv))
print("The arguments are:" , str(sys.argv))

url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(sys.argv[1])).json()
todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

print("User request are : {}".format(user))

print("Todo request are : {}".format(todos))

completed = [t.get("title") for t in todos if t.get("completed") is True]
print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
[print("\t {}".format(c)) for c in completed]


user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(user_id)).json()
username = user.get("username")
todos = requests.get(url + "todos", params={"userId": user_id}).json()

with open("{}.csv".format(user_id), "w", newline="") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    [writer.writerow(
        [user_id, username, t.get("completed"), t.get("title")]
        ) for t in todos]




user_id = sys.argv[1]
url = "https://jsonplaceholder.typicode.com/"
user = requests.get(url + "users/{}".format(user_id)).json()
username = user.get("username")
todos = requests.get(url + "todos", params={"userId": user_id}).json()

with open("{}.json".format(user_id), "w") as jsonfile:
    json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, jsonfile)



url = "https://jsonplaceholder.typicode.com/"
users = requests.get(url + "users").json()

with open("todo_all_employees.json", "w") as jsonfile:
    json.dump({
        u.get("id"): [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": u.get("username")
        } for t in requests.get(url + "todos",
                                params={"userId": u.get("id")}).json()]
        for u in users}, jsonfile)

#     { "USER_ID": [ 
#     {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, 
#     {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], 
#   "USER_ID": [ 
#       {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, 
#       {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}