#!/usr/bin/python3
#!/usr/bin/python3


"""
script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
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

        Function that gets the arguments form stdout

        Return: db object
        """
    args = sys.argv
    host = "localhost"
    port = 3306
    user = args[1]
    password = args[2]
    database = args[3]
    matching_argument = args[4]

    db = MySQLdb.connect(host=host, port=port, passwd=password,
                         user=user, db=database)
    cursor_objects = db.cursor()

    return db, matching_argument, cursor_objects


def query_select(db, matching_argument, cursor_objects):
    """Selects all the row from the database and sorts them
        in ascending order by states.id and displays them"""

    cursor_objects.execute("""SELECT * FROM states WHERE name = "{:s}"
     ORDER BY id ASC""".format(matching_argument))
    for row in cursor_objects.fetchall():
        print(row)


if __name__ == "__main__":
    db, matching_argument, cursor_objects = connect_to_database()
    query_select(db, matching_argument, cursor_objects)
    db.close()
    cursor_objects.close()
