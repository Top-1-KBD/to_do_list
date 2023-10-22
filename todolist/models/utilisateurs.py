"""Module for managing user data and.

authentication in the ToDoList application.

This module defines the `User` class for representing user data,

provides functions for user authentication,

and manages user data storage in an SQLite database.
"""

from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


class User:
    """Class representing a user."""

    def __init__(self, username, password, role='USER'):
        """Initialize a new user with the given username, password, and role.

        Args:
            username (str): The username of the user.
            password (str): The password of the user (hashed).
            role (str, optional): The role of the user (default is 'USER').
        """
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    @classmethod
    def fetch_user(cls, username):
        """Fetch a user from the database by username.

        Args:
            username (str): The username to fetch.

        Returns:
            User or None: The user object if found, None otherwise.
        """
        user_data = get_user(username)
        if user_data:
            username, password_hash, role = user_data
            user = cls(username, password_hash, role)
            user.password_hash = password_hash
            return user
        return None

    def check_password(self, password):
        """Check if the given password matches the user's password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return check_password_hash(self.password_hash, password)


# Fonction to retrieve a user from SQLite
def get_user(username):
    """Retrieve a user from the SQLite database by username.

    Args:
        username (str): The username to retrieve.

    Returns:
        tuple or None: A tuple with user data,
        (username, password hash, role) if found, None otherwise.
    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()


class Database:
    """Class representing a user database."""

    def __init__(self):
        """Initialize a new database."""
        self.users_db = {}  # Use a dictionary to store users

    def add_user(self, username, password):
        """Add a user to the database.

        Args:
            username (str): The username of the user.
            password (str): The password of the user (hashed).

        Returns:
            bool: True if the user was added, False if the user already exists.
        """
        if username not in self.users_db:
            user = User(username, password)
            self.users_db[username] = user
            return True
        return False

    def get_user(self, username):
        """Retrieve a user from the database by username.

        Args:
            username (str): The username to retrieve.

        Returns:
            User or None: The user object if found, None otherwise.
        """
        return self.users_db.get(username)

# Create an instance of the database
# to be used in other parts of your application


users_db = Database()
