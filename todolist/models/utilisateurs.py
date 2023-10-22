"""Module for user-related classes and functions."""

from werkzeug.security import generate_password_hash, check_password_hash
from .roles import Role


class User:
    """Class representing a user."""

    def __init__(self, username, password, role=Role.USER):
        """Init a new user with the given username, password, and role."""
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        """Check if the given password matches the user's password."""
        return check_password_hash(self.password_hash, password)


users_db = {}
