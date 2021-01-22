#!/usr/bin python3
import input_check
import csv
import ceaser_cypher

def login_query():
    """Login interface for signing into websites. Prompts the user for login details."""

    while True:
        user_input = input("Hello Friend. Do you want to sign in [S] or create [C] a new account?\n")

        if user_input in "Ss":
            login_existing()
            break
        elif user_input in "Cc":
            create_new()
            login_existing()
            break
        else:
            print("Incorrect input. Type S for signing in or C for creating a enw account.")
            continue

def login_existing():
    """Signing in existing users."""

    entry = False
    login_attempts = 1

    # Check username and password in database:
    while True:
        if login_attempts <= 3:
            username = str(input("Name:\n"))
            password = str(input("Password:\n"))

            with open ("user_data.csv", "r") as f_csv:
                user_reader = csv.DictReader(f_csv)
                for row in user_reader:
                    if username == row["username"] and password == ceaser_cypher.ceaser_cypher_decoder(row["password"]):
                        entry = True
                        break
            if entry == True:
                return print("Hi {}. You are logged in successfully.\n".format(username))
            else:
                print("We cannot find this username or password.")
                login_attempts += 1
                continue
        else:
            return print("You have failed to sign in three times. Your account is locked now. Please contact admin.")

def create_new():
    """Create new user account and store password."""

    # Create and check username:
    while True:
        username = str(input("What will be your login name?\n"))
        if not input_check.character_check(username, "username", 5, 10, r"[^\w\.]+") or not input_check.uniqueness_check(username, "user_data.csv"):
            continue
        else:
            break

    # Create and check password:
    while True:
        password = str(input("What will be your password?\n"))
        if not input_check.character_check(password, "password", 3, 10, r"[^\w]+"):
            continue
        else:
            break

    # Encode password:
    password = ceaser_cypher.ceaser_cypher_encoder(password)

    # Save password:
    with open ("user_data.csv", "a") as f_csv:
        user_data = [username, password]
        user_writer = csv.writer(f_csv)
        user_writer.writerow(user_data)

    return print("Your new account is created successfully. Now you can sign in.")

login_query()
