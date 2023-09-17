#!/usr/bin/python3

'''
Lists all cities from a database
'''


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute(
        """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states on states.id=cities.state_id
        """
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
