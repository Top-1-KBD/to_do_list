
"""
Module responsible for database operations related to users.
Contains methods to initialize the database, add users, and fetch user details.
"""

import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = 'users.db'


def init_db():
    
    """
    Init the db by creating the required tables if they don't exist.
    Specifically, it creates a 'users' table.
    with columns for username (as primary key),
    password hash, and user role.
    """
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT,
            role TEXT
        )
        ''')
        conn.commit()


def add_user_to_db(username, password):
    """
    Add a new user to the database.

    Args:
        username (str): The username of the new user.
        password (str): The password for the new user,
        which will be hashed before storage.

    Raises:
        Exception: If a user,
        with the given username already exists in the database.
    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        password_hash = generate_password_hash(password)
        try:
            cursor.execute(
                "INSERT INTO users (username, password_hash, role)"
                "VALUES (?, ?, ?)",
                (username, password_hash, 'USER')
            )
            conn.commit()
        except sqlite3.IntegrityError:
            raise Exception("Username already exists!")


def get_user(username):
    """
    Fetch a user from the database based on the given username.

    Args:
        username (str): The username of the user to fetch.

    Returns:
        tuple: A tuple containing the user's username, password hash, and role.
              If no user is found, returns None.
    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT username, password_hash,"
            "role FROM users WHERE username = ?",
            (username,)
        )
        user = cursor.fetchone()
        return user


init_db()  # Initialization of the database when importing the module
