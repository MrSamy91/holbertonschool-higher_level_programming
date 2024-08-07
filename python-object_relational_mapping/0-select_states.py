#!/usr/bin/python3
import MySQLdb
import sys

def list_states():
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all the results
    states = cursor.fetchall()

    # Print the results
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    list_states()
