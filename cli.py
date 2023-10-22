import argparse
from todolist.models.database import init_db
from todolist.models.database import init_db, add_user_to_db

def initialize_database():
    print("Initialising the database...")
    init_db()
    print("Database initialized successfully!")

def add_user(username, password):
    try:
        add_user_to_db(username, password)
        print(f"User {username} added successfully!")
    except Exception as e:
        print(f"Failed to add user: {e}")

def main():
    parser = argparse.ArgumentParser(description='CLI for TO_DO_LIST application.')

    parser.add_argument('--initdb', action='store_true', help='Initialize the database.')
    parser.add_argument('--adduser', nargs=2, metavar=('USERNAME', 'PASSWORD'), help='Add a user.')

    args = parser.parse_args()

    if args.initdb:
        initialize_database()
    if args.adduser:
        username, password = args.adduser
        add_user(username, password)

if __name__ == '__main__':
    main()