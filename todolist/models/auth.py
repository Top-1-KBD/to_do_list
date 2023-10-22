from models.utilisateurs import User, users_db


def register(username, password):
    if username in users_db:
        raise ValueError("User already exists")
    user = User(username, password)
    users_db[username] = user


def login(username, password):
    user = users_db.get(username)
    if user and user.check_password(password):
        return {"status": "logged in", "username": username}
    else:
        return {"status": "failed"}


def logout(session):
    session.clear()  # Simule un dictionnaire de session
