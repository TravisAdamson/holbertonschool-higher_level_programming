#!/usr/bin/python3
""" Contains MySQLdb script that prints states starting with given letter"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' "
                   "ORDER BY id ASC".format(sys.argv[4]))

    states = cursor.fetchall()

    for state in states:
        if state[1][0] == sys.argv[4]:
            print(state)

    cursor.close()
    db.close()
