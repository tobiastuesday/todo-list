# To-do list thing

import json
from datetime import datetime


def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_new_tasks(task_list):
    new_tasks = input("Enter your tasks (separate with commas): ").split(", ")
    for task in new_tasks:
        new_task_item = {
            "Task": task,
            "Timestamp": datetime.now().isoformat(),
            "Status": "Pending"
        }
        task_list.append(new_task_item)


def store_tasks(all_tasks):
    with open("tasks.json", "w") as file:
        json.dump(all_tasks, file, indent=4)


# run program
my_tasks = load_tasks()
add_new_tasks(task_list=my_tasks)
store_tasks(all_tasks=my_tasks)
print("Your tasks have been saved to tasks.json")
