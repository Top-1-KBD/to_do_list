"""Module for authentication-related functions."""

from models.utilisateurs import User, users_db


def register(username, password):
    """Register a new user with the given username and password."""
    if username in users_db:
        raise ValueError("User already exists")
    user = User(username, password)
    users_db[username] = user


def login(username, password, session):
    """Log in a user with the given username and password."""
    user = users_db.get(username)
    if user and user.check_password(password):
        session['username'] = username  # Stocker le nom d'utilisateur dans la session
        return {"status": "logged in", "username": username}
    else:
        return {"status": "failed"}


def logout(session):
    """Log out the current user."""
    session.clear()  # Simule un dictionnaire de session
