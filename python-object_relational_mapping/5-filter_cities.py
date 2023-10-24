#!/usr/bin/python3
""" Contains MySQLdb script that prints states starting with given letter"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    query = '''SELECT *
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC;
            '''
    c.execute(query)

    cities = c.fetchall()

    for city in cities: 
        if city[4] == argv[4]:
            print_cities = city[2]
    print(', '.join(print_cities))

    c.close()
    db.close()
