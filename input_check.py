import re

def password_check(password):
    """Checks if the password complies with the requirements"""

    if 3 > len(password) > 10:
        return print("The password must be between 3 and 10 characters.")

    characters = r"[\w]+"
    if not re.search(characters, password):
        return print("The password can only contain letters, numbers and underscores.")
    else:
        return True
