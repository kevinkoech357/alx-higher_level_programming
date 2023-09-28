#!/usr/bin/python3

'''
Takes in the name of a state as an argument and lists all cities of that state
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
        SELECT cities.name
        FROM cities
        INNER JOIN states on states.id=cities.state_id
        WHERE states.name=%s""", (sys.argv[4],)
    )

    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))

    cur.close()
    db.close()
