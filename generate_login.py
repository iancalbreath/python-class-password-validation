# Mac Littlefield's class
# Driver for lab 8

# Gets users first, last and ID no. and generates uniform system username

import login

def main():
    # get users' first, last and ID no
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    # Get login name
    print('Your system login name is:')
    print(login.get_login_name(first, last, idnumber))

# Call main

main()
