#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
This script lists all states from hbtn_0e_0_usa db
'''


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

    db.close()
