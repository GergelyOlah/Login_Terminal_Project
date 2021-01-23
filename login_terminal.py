#!/usr/bin python3
import input_check
import csv
import ceaser_cypher
import login_time
import network_check
from datetime import datetime

def login_query():
    """Login interface for signing into websites. Prompts the user for login details."""

    while True:
        user_input = input("Hello Friend. Do you want to sign in [S] or create [C] a new account?\n")

        if user_input in "Ss":
            login_existing()
            network_check.result()
            break
        elif user_input in "Cc":
            create_new()
            login_existing()
            network_check.result()
            break
        else:
            print("Incorrect input. Type S for signing in or C for creating a new account.")
            continue

def login_existing():
    """Signing in existing users."""

    entry_data = False
    login_attempts = 1

    # Ask for login detials:
    while True:
        if login_attempts <= 3:
            username = str(input("Name:\n"))
            password = str(input("Password:\n"))
            login_attempt_time = datetime.today().replace(microsecond=0)

            # Check username and password in database:
            with open ("user_data.csv", "r") as f_csv:
                user_reader = csv.DictReader(f_csv)
                for row in user_reader:
                    if username == row["username"] and password == ceaser_cypher.ceaser_cypher_decoder(row["password"]):
                        entry_data = True
                        break

            # Check if account is locked:
            if entry_data == True and login_time.check(username, login_attempt_time, "user_data.csv") == True:
                login_time.update(username, login_attempt_time, "user_data.csv", "N")
                return print("\nHi {}. You are logged in successfully.".format(username))

            elif entry_data == True and login_time.check(username, login_attempt_time, "user_data.csv") != True:
                return print("Your account is still locked due to too many failed login attempts. Please try again later or contact admin.")

            else:
                print("We cannot find this username or password.")
                login_time.update(username, login_attempt_time, "user_data.csv", "N")
                login_attempts += 1
                continue
        else:
            login_time.update(username, login_attempt_time, "user_data.csv", "Y")
            return print("You have failed to sign in three times. Your account is locked now for two minutes. Please try again later or contact admin.")

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

    # Asking for additional data:
    email = str(input("What is your email address? \n"))

    # Time of account creation:
    initiation = datetime.today().replace(microsecond=0)

    # Save data into database:
    with open ("user_data.csv", "a") as f_csv:
        user_data = [username, password, email, initiation, initiation, "N"]
        user_writer = csv.writer(f_csv)
        user_writer.writerow(user_data)

    return print("Your new account is created successfully. Now you can sign in.")

login_query()
