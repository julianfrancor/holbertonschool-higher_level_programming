#!/usr/bin/python3


"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


def connect_to_database():
    """Function that reads arguments from stdout
        and creates a connection to the MySQL server
        running on the local machine via a
        UNIX socket(host and port) (or named pipe),
        the user name = args[1], password = args[2],
        and selects the database args[3].

        Return: db object
        """
    args = sys.argv
    host = "localhost"
    port = 3306
    user = args[1]
    password = args[2]
    database = args[3]

    db = MySQLdb.connect(host=host, port=port, passwd=password,
                         user=user, db=database)

    return db


def query_select(db):
    """Selects all the row from the database and sorts them
        in ascending order by states.id and displays them"""

    db.query("""SELECT * FROM states ORDER BY id ASC""")
    result = db.store_result()
    for row in result.fetch_row(0):
        print(row)


if __name__ == "__main__":
    db = connect_to_database()
    query_select(db)
    db.close()
