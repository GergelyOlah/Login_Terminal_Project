import re

def username_check(username):
    """Checks if the password complies with the requirements"""
    if len(password) < 5 or len(password) > 10:
        return print("The username must be between 3 and 10 characters.")

    characters = r"[^\w]+"
    if len(re.findall(characters, password)) != 0:
        return print("The username can only contain letters, numbers and underscores.")
    else:
        return True

def password_check(password):
    """Checks if the password complies with the requirements"""

    if len(password) < 3 or len(password) > 10:
        return print("The password must be between 3 and 10 characters.")

    characters = r"[^\w]+"
    if len(re.findall(characters, password)) != 0:
        return print("The password can only contain letters, numbers and underscores.")
    else:
        return True
