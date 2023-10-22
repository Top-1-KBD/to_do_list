import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

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
        password_hash = generate_password_hash(password)  # Assurez-vous d'importer cette fonction depuis werkzeug.security
        try:
            cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", (username, password_hash, 'USER'))
            conn.commit()
        except sqlite3.IntegrityError:
            # Ce bloc sera exécuté si l'ajout de l'utilisateur échoue en raison d'un doublon (car le champ username est une clé primaire).
            raise Exception("Username already exists!")

def get_user(username):
    with sqlite3.connect('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT username, password_hash, role FROM users WHERE username = ?', (username,))
        user = cursor.fetchone()
        return user

init_db()  # Initialisation de la base de données lors de l'import du module
