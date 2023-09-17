#!/usr/bin/python3

'''
Takes user input and displays where name == user_input
'''


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    user_input = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'
                ORDER BY id ASC" .format(user_input))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
