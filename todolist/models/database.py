"""
Module for managing user data in the ToDoList application database.

This module provides functions for initializing the database, adding users,
and getting user data.
"""

import sqlite3

def init_db():
    """
    Initialize the database.

    Creates the 'users' table if it does not exist.

    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        ''')
        conn.commit()

def add_user(username, password):
    """
    Add a new user to the database.

    Args:
        username (str): The username of the new user.
        password (str): The password for the new user (hashed before storage).

    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) "
            "VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

def get_user(username):
    """
    Get user data by username.

    Args:
        username (str): The username of the user to retrieve.

    Returns:
        tuple: A tuple containing user data (id, username, password) if found,
        or None if not found.

    """
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()