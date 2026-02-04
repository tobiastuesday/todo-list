# To-do list thing

def enter_tasks():
    tasks = input("Enter your tasks: ").split(", ")
    return tasks


def store_tasks(tasks):
    with open("tasks.txt", "a") as file:
        for task in tasks:
            file.write(task + "\n")


# run program
tasks = enter_tasks()
store_tasks(tasks)
print("Your tasks have been saved to tasks.txt")
