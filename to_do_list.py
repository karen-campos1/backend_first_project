# #To-Do List Features:
# Implement the following features for the To-Do List:
# Adding a task
# Viewing the list of tasks with from Incomplete and Complete tasks.
# Marking a task as complete.
# Deleting a task.
# Quitting the application.
# User Interaction:
# Allow users to interact with the application by selecting menu options using input().
# Implement input validation to handle unexpected user input gracefully.
# Error Handling:
# Implement error handling using try, except, else, and finally blocks to handle potential issues.
# Code Organization:
# Organize your code into functions to promote modularity and readability.
# Use meaningful function names with appropriate comments and docstrings for clarity.
# Testing and Debugging:
# Consider edge cases, such as empty task lists or incorrect user input.


# welcome = """Welcome to the To-Do List App!
#     Menu:
#     1. Add a task
#     2. View tasks
#     3. Mark a task as complete
#     4. Delete a task
#     5. Quit"""
# print(welcome) 

#empty global lists:
completed_tasks = []
incomplete_tasks = []

#no. 1 on menu - ADD
def add_task():
    task = input("What task would you like to add? ").lower()
    if task not in incomplete_tasks:
        incomplete_tasks.append(task)
        print(f"Your 'To Do List' is now: {incomplete_tasks} ")
    else:
        print("That task is already on your 'To Do List' :)")

#skipped no. 2 "view tasks" no function built for it, move on to no.3 "mark tasks"

#no. 3 on menu - MARK
def mark_task():
    task = input("To mark a task on your 'To Do List' as 'done' enter 1 otherwise enter 2 to exit: \n")
    if task == "1":
        try:
            print(f"Your current 'To Do List' includes {incomplete_tasks}")
            completed_task = input("From that list what task would you like to mark as done?: ").lower()
            incomplete_tasks.remove(completed_task)
            completed_tasks.append(completed_task)
            print(f"You've successfully updated your 'To Do List.' Your completed tasks are: {completed_tasks}")
        except ValueError:
            print(f"{completed_task} is not valid, you must enter EXACTLY as shown on your list!") 
    elif task == "2":
        print("No tasks will be altered.")
    else:
        print("Please enter a valid response of 1 or 2! You are being returned to the Main Menu.")
     
          
#no. 4 on menu - REMOVE         
def delete_task():
    task = input(f"What task are you looking to delete? {incomplete_tasks} {completed_tasks} : ").lower()
    if task in incomplete_tasks:
        response = input(f"Are you sure you want to DELETE '{task}' task? enter yes/no ").lower()
        if response.lower() == "yes":
            incomplete_tasks.remove(task)
            print(f"Your updated 'To Do List' is now: {incomplete_tasks}")
        elif response.lower() == "no":
            print("Nothing has been deleted.")
        else:
            print("INVALID response")
    elif task in completed_tasks:
        response = input(f"Are you sure you want to DELETE '{task}' task? enter yes/no ").lower()
        if response.lower() == "yes":
            completed_tasks.remove(task)
            print(f"Your updated completed tasks are now: {completed_tasks}")
        elif response.lower() == "no":
            print("Nothing has been deleted.")  
        else:
            print("INVALID RESPONSE")
    try:
        completed_tasks.remove(task)
    except ValueError:
        print(f"{task} is not in your Completed-Tasks, you can't remove something that doesn't exist!")
    try:
        incomplete_tasks.remove(task)
    except ValueError:
        print(f"{task} is not on your 'To Do List', you can't remove something that doesn't exist!")
        
        
# DRIVER CODE
def run_app():
    while True:
        
        response = input("""\nWelcome to the To-Do List App!
    Menu: Pick one
        1. Add a task
        2. View tasks
        3. Mark a task as complete
        4. Delete a task
        5. Quit
        """)
        if response == "1":
            add_task()
        elif response == "2":
            print(f"Your current 'To Do List' is: {incomplete_tasks} \n Your completed tasks are: {completed_tasks}")
        elif response == "3":
            mark_task()
        elif response == "4":
            delete_task()
            print("You're being returned to the main menu. ")
        elif response == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5." )
run_app()