#!/usr/bin python3
import csv
import datetime

def check(username, time, database):
    """Checks if the minimum time has elapased since the last failed login attempt."""

    current_time = datetime.datetime.today().replace(microsecond=0)
    time_limit = current_time - datetime.timedelta(minutes = 10)

    with open (database, "r") as f_csv:
        user_reader = csv.DictReader(f_csv)

        for row in user_reader:
            if row["username"] == username:
                if row["locked"] == "N":
                    return True
                elif datetime.datetime.strptime(row["last_login"], "%Y-%m-%d %H:%M:%S") < time_limit:
                    return True
                else:
                    break

def update(username, time, database, result):
    """Update the login time and result in database."""

    row_updated = None

    # Find the data for the user:
    with open (database, "r") as f_csv:
        user_reader = csv.reader(f_csv)
        user_data_list = list(user_reader)

        for i in range(len(user_data_list)):
            if user_data_list[i][0] == username:
                row_updated = user_data_list[i]
                index = i

    # Updat user date:
    if row_updated == None:
        return
    else:
        row_updated[4] = time
        row_updated[5] = result
        user_data_list[index] = row_updated

    # Write updated user data back to the database:
    with open (database, "w") as f_csv:
        user_writer = csv.writer(f_csv)
        user_writer.writerows(user_data_list)

update("Ursula", datetime.datetime.today(), "user_data.csv", "Y")
