"""CLI Module for the ToDoList application.

This module provides command line utilities.

to interact with the ToDoList application.

You can use this CLI to add tasks, remove tasks,

list tasks, list users, and initialize the database.
"""

import argparse
from todolist.models.task_list import TaskList
from todolist.models.utilisateurs import users_db
from todolist.models.database import init_db, add_user
from todolist.exceptions.task_exceptions import TaskNotFoundError


def initialize_database():
    """Initialize the database."""
    init_db()
    print("Database initialized successfully!")


def add_user_to_db(username, password):
    """Add a user to the database."""
    try:
        add_user(username, password)
        print(f"User {username} added successfully!")
    except Exception as e:
        print(f"Failed to add user: {e}")


def add_task(task_list):
    """Add a task to the task list."""
    name = input("Enter task name: ")
    description = input("Enter task description: ")
    task_list.add_task(name, description)
    print("Task added successfully!")


def remove_task(task_list):
    """Remove a task from the task list."""
    name = input("Enter task name to remove: ")
    try:
        task_list.remove_task(name)
        print("Task removed successfully!")
    except TaskNotFoundError as e:
        print(f"Error: {e}")


def list_tasks(task_list):
    """List all tasks in the task list."""
    tasks = task_list.display_tasks()
    if tasks:
        print("Tasks:")
        for task in tasks:
            print(task)
    else:
        print("No tasks found.")


def list_users():
    """List all users in the user database."""
    if users_db:
        print("Users:")
        for username, user in users_db.items():
            print(f"Username: {username}, Role: {user.role}")
    else:
        print("No users found.")


def main():
    """Serve main entry point for the ToDoList CLI."""
    task_list = TaskList()

    parser = argparse.ArgumentParser(
        description='CLI for ToDoList application.'
    )
    parser.add_argument(
        '--initdb',
        action='store_true',
        help='Initialize the database.'
    )
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
        add_user_to_db(username, password)

    while True:
        print("Choose an option:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. List Tasks")
        print("4. List Users")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            remove_task(task_list)
        elif choice == "3":
            list_tasks(task_list)
        elif choice == "4":
            list_users()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == '__main__':
    main()
