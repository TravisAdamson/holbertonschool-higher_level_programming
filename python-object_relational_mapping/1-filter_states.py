#!/usr/bin/python3
""" Contains MySQLdb script that gets all states that start with "N" from given table """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)

    cursor.close()
    db.close()
