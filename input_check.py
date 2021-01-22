import re


def character_check( text, text_type, min_length, max_length, characters):
    """Checks if the input text complies with the requirements"""

    if len(text) < min_length or len(text) > max_length:
        return print("The {} must be between {} and {} characters.".format(text_type, min_length, max_length))

    if len(re.findall(characters, text)) != 0:
        return print("The {} can only contain letters, numbers and underscores.".format(text_type))
    else:
        return True

def uniqueness_check(text, database):
    pass
