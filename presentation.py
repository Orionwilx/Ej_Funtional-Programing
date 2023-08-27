def show_tasks(tasks):
    print("Task List:")
    for task in tasks:
        print("-", task)

def get_new_task():
    return input("Enter a new task: ")
