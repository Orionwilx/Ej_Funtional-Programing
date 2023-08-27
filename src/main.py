import presentation.presentation as presentation
import business_logic2.business_logic as business_logic
import data_persistence.data_persistence as data_persistence
from os import system

while True:
    print("\n1. Add Task")
    print("2. Complete Task")
    print("3. Show Incomplete Tasks")
    print("4. Exit")
    option = input("Select an option: ")
    system('cls')

    if option == "1":
        new_task = presentation.get_new_task()
        data_persistence.tasks = business_logic.add_task(data_persistence.tasks, new_task)
        system('cls')

    elif option == "2":
        completed_task = input("Enter the completed task: ")
        data_persistence.tasks = business_logic.complete_task(data_persistence.tasks, completed_task)
        system('cls')

    elif option == "3":
        incomplete_tasks = business_logic.filter_incomplete_tasks(data_persistence.tasks)
        presentation.show_tasks(incomplete_tasks)

    elif option == "4":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")
