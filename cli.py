"""CLI Module for the ToDoList application.

Provides command line utilities to interact with the application.
"""

import argparse
from todolist.models.database import init_db, add_user_to_db
from todolist.models.task_list import TaskList
from todolist.models.utilisateurs import Role
from todolist.models.utilisateurs import users_db
from todolist.exceptions.task_exceptions import TaskNotFoundError


def initialize_database():
    """
    Initialize the database.

    Displays messages about the status of the initialization process.
    """
    print("Initialising the database...")
    init_db()
    print("Database initialized successfully!")


def add_user(username, password):
    """
    Add a user to the database.

    Args:
        username (str): The username to adds.
        password (str): The password for the user.

    Displays a success message if the user is added successfully,
    and an error message if there is an issue.
    """
    try:
        add_user_to_db(username, password, Role.USER)
        print(f"User {username} added successfully!")
    except Exception as e:
        print(f"Failed to add user: {e}")


def add_task():
    """
    Add a task to the task list.
    """
    task_list = TaskList()
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    task_list.add_task(name, description)
    print("Task added successfully!")


def remove_task():
    """
    Remove a task from the task list.
    """
    task_list = TaskList()
    name = input("Enter task name to remove: ")
    try:
        task_list.remove_task(name)
        print("Task removed successfully!")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


def list_tasks():
    """
    List all tasks in the task list.
    """
    task_list = TaskList()
    tasks = task_list.display_tasks()
    for task in tasks:
        print(task)


def list_users():
    """
    List all users in the user database.
    """
    for username, user in users_db.items():
        print(f"Username: {username}, Role: {user.role}")


def main():
    """
    Serve as the main entry point for the CLI.

    Processes command line arguments and executes the requested operations.
    """
    parser = argparse.ArgumentParser(description='CLI for TDL application.')
    parser.add_argument('--initdb', action='store_true', help='Init the db.')
    parser.add_argument(
                        '--adduser',
                        nargs=2,
                        metavar=('USERNAME', 'PASSWORD'),
                        help='Add a user.'
                        )

    args = parser.parse_args()

    if args.initdb:
        initialize_database()
    if args.adduser:
        username, password = args.adduser
        add_user(username, password)

    while True:
        print("Choose an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. List Users")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            list_tasks()
        elif choice == "4":
            list_users()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()
