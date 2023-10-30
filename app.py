"""This file contains the main entry point for the application."""


from bin.create_user import create_user
from bin.connect_user import connect_user
from bin.create_task import create_task

print("Welcome to the todolist application!")
print("This application allows you to manage your tasks.")

CHOICE = ""
while CHOICE != "3":

    print("Please select an option:")
    print("1. Create a new account")
    print("2. Connect to your account")
    print("3. Quit")

    CHOICE = input("Enter your choice: ")

    if CHOICE == "1":
        create_user()
    elif CHOICE == "2":
        user_id, is_connected = connect_user()
        if is_connected:
            print("You are now connected!")
            print("You can now manage your tasks.")
            print("What do you want to do?")
            print("1. Create a new task")
            print("2. List all your tasks")
            print("3. Change a task status")
            print("4. Delete a task")
            print("5. Return to the previous menu")
            choice_action = input("Enter your choice: ")

            if choice_action == "1":
                print("You selected 'Create a new task'")
                create_task()
            elif choice_action == "2":
                print("You selected 'List all your tasks'")
            elif choice_action == "3":
                print("You selected 'Change a task status'")
            elif choice_action == "4":
                print("You selected 'Delete a task'")

        else:
            print("Failed to connect. Please try again.")
    elif CHOICE == "3":
        print("Thanks you!")
    else:
        print("Invalid choice. Please try again.")
