#!/usr/bin/python3
<<<<<<< HEAD
"""  lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
=======
""" Lists all states from the database htbn_0e_0_usa """
import MySQLdb
import sys

if __name == "__main__":
	db = MySQLdb.connect(host="localhost", user=sys.argv[1],
		passwd=sys.argv[2], db=sys.argv[3], port=3306)
	cur = db.cursor()
	match = sys.argv[4]
	cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
	rows = cur.fetchall()
	for row in rows:
		print(row)
	cur.close()
	db.close()

>>>>>>> 78aa71b2e5b25312c7c2cf5cc78d309c4d029958
