#!/usr/bin/python3

"""
This module contains a script that lists
all states in a database
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id"
    rows = cursor.execute(query)

    for row in range(rows):
        print(cursor.fetchone())

    cursor.close()
    db.close()
