# This program gets a password from the user and validates it

import login

def main():
        # Gets password from user
        password = input('Enter your password: ')

        # Validate password
        while not login.valid_password(password):
            print('That password is not valid.')
            password = input('Enter your password: ')

        print('That is a valid password.')
# call main

if __name__ == '__main__':
    main()
