# To-do list thing

from datetime import datetime


def enter_tasks():
    tasks = input("Enter your tasks: ").split(", ")
    return tasks


def store_tasks(tasks):
    current_date = datetime.now()
    with open("tasks.txt", "a") as file:
        for task in tasks:
            file.write(task + "\n")
        file.write(str(current_date))


# run program
tasks = enter_tasks()
store_tasks(tasks)
print("Your tasks have been saved to tasks.txt")
