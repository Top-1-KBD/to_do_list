"""Module for authentication-related functions."""

# authentication.py

from werkzeug.security import generate_password_hash, check_password_hash
from .database import add_user, get_user

# Enregistre un nouvel utilisateur

def register(username, password):
    hashed_password = generate_password_hash(password)
    add_user(username, hashed_password)

# Connecte un utilisateur

def login(username, password):
    user = get_user(username)
    if user and check_password_hash(user[2], password):
        return True
    return False
