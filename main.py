#!/usr/bin python3

#Check empty, check character set, save password, log out after 3 tries. Store additional data for account recovery (phone number, birthdate, memorable word)
import csv

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
            print("Incorrect input.")
            continue

def login_existing():
    """Signing in existing users."""

    entry = False
    while True:
        account_name = str(input("Name:\n"))
        password = str(input("Password:\n"))

        with open ("user_data.csv", "r") as f_csv:
            user_reader = csv.DictReader(f_csv)
            for row in user_reader:
                if account_name == row["username"] and password == row["password"]:
                    entry = True
                    break
            if entry == True:
                return print("Hi {}. You are logged in successfully.\n".format(account_name))
            else:
                print("We cannot find this username or password.")
                continue

def create_new():
    """Create new user account and store password."""

    account_name = str(input("What will be your login name?\n"))
    password = str(input("What will be your password?\n"))
    with open ("user_data.csv", "a") as f_csv:
        user_data = [account_name, password]
        user_writer = csv.writer(f_csv)
        user_writer.writerow(user_data)

    return print("Your new account is created successfully. Now you can sign in.")

login_query()
