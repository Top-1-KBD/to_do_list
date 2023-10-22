"""Module for user-related classes and functions."""

from werkzeug.security import generate_password_hash, check_password_hash


class User:
    """Class representing a user."""
    def __init__(self, username, password):
        """Initialize a new user with the given username and password."""
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check if the given password matches the user's password."""
        return check_password_hash(self.password_hash, password)


users_db = {}
