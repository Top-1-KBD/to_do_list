"""

Module responsible for the User model.
Defines the User class which represents an individual user, their attributes,
and methods related to user authentication and interaction with the database.
"""

from werkzeug.security import generate_password_hash, check_password_hash
from .roles import Role
# Importez les fonctions de la base de données
from .database import add_user, get_user


class User:
    """Class representing a user."""

    def __init__(self, username, password, role=Role.USER):
        """Init a new user with the given username, password, and role."""
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role
        # Ajoutez l'utilisateur à la base de données
        if not add_user(username, password, role):
            raise ValueError(f"Nom d'utilisateur '{username}' déjà pris")

    @classmethod
    def fetch_user(cls, username):
        """Fetch a user from the database by username."""
        user_data = get_user(username)
        if user_data:
            username, password_hash, role = user_data
            user = cls(username, password_hash, role)
            # Utilisez le hash du mot de passe directement
            user.password_hash = password_hash
            return user
        return None

    def check_password(self, password):
        """Check if the given password matches the user's password."""
        return check_password_hash(self.password_hash, password)
