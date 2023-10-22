import sqlite3

# Initialise la base de données


def init_db():
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

# Ajoute un utilisateur à la base de données


def add_user(username, password):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users (username, password) "
            "VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

# Obtient un utilisateur par nom d'utilisateur


def get_user(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        return cursor.fetchone()
