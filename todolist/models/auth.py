"""Module for authentication-related functions."""

# authentication.py

from werkzeug.security import generate_password_hash, check_password_hash
from .database import add_user, get_user

# Enregistre un nouvel utilisateur


def register(username, password):
    """Register a new user with the given username and password.
    Args:
        username (str): The username of the new user.
        password (str): The password for the new user.

    Returns:
        bool: True if the user was successfully registered, False otherwise.

    This function adds a new user to the user database. If the username is already,
    in use, the registration will fail and return False. Otherwise, the user is,
    registered, and True is returned.
    """
    hashed_password = generate_password_hash(password)
    add_user(username, hashed_password)

# Connecte un utilisateur


def login(username, password):
    """Log in a user with the given username and password.
    Args:
        username (str): The username of the user attempting to log in.
        password (str): The password provided by the user for authentication.

    Returns:
        bool: True if the login is successful, False otherwise.

    This function checks if the provided user exists in the user database and if
    the provided PW matches the stored PW hash for that username. If both
    conditions are met, the login is considered successful, and True is returned.
    Otherwise, the login fails, and False is returned.
    """
    user = get_user(username)
    if user and check_password_hash(user[2], password):
        return True
    return False
