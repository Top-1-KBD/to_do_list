# utilisateurs.py

from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3


class User:
    """Class representing a user."""

    def __init__(self, username, password, role='USER'):
        """Init a new user with the given user, password, and role."""
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.role = role

    @classmethod
    def fetch_user(cls, username):
        """Fetch a user from the database by username."""
        user_data = get_user(username)
        if user_data:
            username, password_hash, role = user_data
            user = cls(username, password_hash, role)
            user.password_hash = password_hash
            return user
        return None

    def check_password(self, password):
        """Check if the given password matches the user's password."""
        return check_password_hash(self.password_hash, password)


# Fonction pour récupérer un utilisateur depuis la base de données SQLite
def get_user(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()


class Database:
    def __init__(self):
        self.users_db = {}  # Utilisez un dictionnaire pour stocker les utilisateurs

    def add_user(self, username, password):
        if username not in self.users_db:
            user = User(username, password)
            self.users_db[username] = user
            return True
        return False

    def get_user(self, username):
        return self.users_db.get(username)

# Créez une instance de la base de données pour être utilisée dans d'autres parties de votre application
users_db = Database()
