# Queries for the NPS Parks database
import sqlite3
import os

db = None


def main():
    global db
    try:
        dbname = 'nps_parks.db'
        if os.path.exists(dbname):  # does this database file exist?
            db = sqlite3.connect(dbname)  # connect to the database

            query_parks_by_state()
            query_parks_by_designation()
            query_parks_by_activity()

            db.close()  # close the database
        else:
            print('Error:', dbname, 'does not exist')

    except sqlite3.IntegrityError as err:
        print('Integrity Error:', err)
    except sqlite3.OperationalError as err:
        print('Operational Error:', err)
    except sqlite3.Error as err:
        print('Error:', err)


def query_parks_by_state():
    # Prompts for the state to list all the National Parks in this state.
    # Continues prompting if the user enters no value.
    cursor = db.cursor()
    state_input = ""
    state_count = 0
    while state_input == "":
        state_input = input("Find National Parks in this state: ")
    # TODO Construct the query that incorporates the user's selection, and display formatted results.
    state_sql = "SELECT Name, Designation, States FROM Park WHERE states LIKE '%" + state_input + "%' "
    # TODO See the assignment description for sample input and output
    print(state_sql)
    cursor.execute(state_sql)
    records = cursor.fetchall()
    for recs in records:
        state_count = state_count + 1
    print(str(state_count) + ' National parks with the designation: ' + state_input)
    for rec in records:
        print(rec)


def query_parks_by_designation():
    # Prompts for the designation to list all the National Parks with this designation.
    # Continues prompting if the user enters no value.
    cursor = db.cursor()
    designation_input = ""
    designation_count = 0
    while designation_input == "":
        designation_input = input("Find National Parks designated as: ")
        # TODO Construct the query that incorporates the user's selection, and display formatted results.
        designation_sql = "SELECT Name, Designation, States FROM Park WHERE designation LIKE '%" + designation_input + "%' "
        print(designation_sql)
    # TODO See the assignment description for sample input and output
    cursor.execute(designation_sql)
    records = cursor.fetchall()
    for rec in records:
        designation_count = designation_count + 1
    print(str(designation_count) + ' National parks with the designation: ' + designation_input)
    for rec in records:
        print(rec)


def query_parks_by_activity():
    # Prompts for an activity to list all the National Parks that support this activity.
    # Continues prompting if the user enters no value.
    cursor = db.cursor()
    activity_input = ""
    activity_count = 0
    while activity_input == "":
        activity_input = input("Find National Parks with this activity: ")
    # Constructs the query that incorporates the user's selection, and display formatted results.
        activity_sql = "SELECT Name, Activity FROM Park JOIN Activities ON park.parkcode = Activities.parkcode AND activity LIKE '%" + activity_input + "%' "
    cursor.execute(activity_sql)
    records = cursor.fetchall()
    for rec in records:
        activity_count = activity_count + 1
    print(str(activity_count) + ' National parks with the designation: ' + activity_input)
    for rec in records:
        print(rec)


main()
