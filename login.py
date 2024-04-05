# Ian Calbreath
# Mac Littlefield's class
# Re-writing password validation programs

# Program 8-6
# The get_login_name func accepts a first name, lastname, and ID as arguments
# It returns a system login name

def get_login_name(first, last, idnumber):
        # Get first 3 letters of first name. >>> CHANGED TO FIRST LETTER OF FIRST NAME
        # if name is less than 3
        # slice will return the entire first name
    set1 = first[0]

    # Get the first 3 of last name >>> CHANGED TO ENTIRE LAST NAME
    # if name is less than 3
    # slice will return entire last name
    set2 = last

    # Get last 3 of student ID
    # If ID is less than 3
    # slice will return the entire ID
    set3 = idnumber[-3 :]

    # Put sets of characters together.
    login_name = set1 + set2 + set3

    # Return the login name.
    return login_name

# valid_password func accepts a pass as an argument and returns
# true or false fto indicate password is valid
# valid pass must be at least 7 chars in length
# have at least 1 uppercase, 1 lower, and 1 digit

def valid_password(password):
    # set the boolean variables to false
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_non_alphanumeric = False  # >>> ADDED NONALPHANUMERIC VARIABLE
    has_space = False             # >>> ADDED NOSPACE VARIABLE
    
    # Begin validation start by testing password length
    if len(password) >= 8:   # >>> CHANGED TO 8
        correct_length = True

        # Test each char and set appropriate flag
        # when required char is found
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True
            if not ch.isalnum():            # >>> ADDED NON ALPHANUMERIC
                has_non_alphanumeric = True
            if ch.isspace():                # >>> ADDED NO SPACE
                has_space = True

            # Determine requirements are met
            # if so, set is_valid to true
            # otherwise, set is_valid to false
    if correct_length and has_uppercase and \
        has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return is_valid variable
    return is_valid
