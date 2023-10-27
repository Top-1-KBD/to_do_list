"""Create a new user"""

import argparse
import getpass
import logging
from models.user import User


def main():
    """This function creates a new user."""

    logging.basicConfig(filename='logs/create_user.log',
                        level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

    parser = argparse.ArgumentParser(description='Create a new user')
    parser.add_argument('username', type=str,
                        help='the username for the new user')
    args = parser.parse_args()

    password = getpass.getpass(prompt='Enter password: ')
    confirm_password = getpass.getpass(prompt='Confirm password: ')
    while password != confirm_password:
        print('Passwords do not match. Please try again.')
        logging.warning('Passwords do not match for user %s', args.username)
        password = getpass.getpass(prompt='Enter password: ')
        confirm_password = getpass.getpass(prompt='Confirm password: ')

    print(f'Creating user {args.username}')
    new_user = User(args.username, password)

    # Later add a verification that the user does not already exist

    print(f'User {args.username} created successfully')
    print(new_user.name, new_user.password)
    logging.info('User %s created successfully', args.username)


if __name__ == '__main__':
    main()
