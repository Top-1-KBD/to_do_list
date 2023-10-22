"""

CLI Module for the ToDoList application.
Provides command line utilities to interact with the application.
"""

import argparse
from todolist.models.database import init_db, add_user_to_db


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

    Adds a user to the database.
    Args:
        username (str): The username to adds.
        password (str): The password for the user.
    Displays a success message if the user is added successfully,
    and an error message if there is an issue.
    """
    try:
        add_user_to_db(username, password)
        print(f"User {username} added successfully!")
    except Exception as e:
        print(f"Failed to add user: {e}")


def main():
    """

    The Main entry point for the CLI.
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


if __name__ == '__main__':
    main()
