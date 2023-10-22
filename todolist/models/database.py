import sqlite3
from werkzeug.security import generate_password_hash

DB_NAME = 'users.db'


def init_db():
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
            # This block is executed if adding the user fails due to a
            # duplicate (because the username field is a primary key).
            raise Exception("Username already exists!")


def get_user(username):
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
