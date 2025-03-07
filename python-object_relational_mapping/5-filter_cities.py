#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        sys.exit(1)

    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query with a JOIN to get cities of the specified state
    # Using parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Extract city names from the results and join them with commas
    cities = [row[0] for row in rows]
    print(", ".join(cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
