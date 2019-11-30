"""CIS189 Python
Author: Greg Tarr
Created: 11/25/2019"""
import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_table(conn, sql_create_table):
    """ Creates table with give sql statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)


def create_tables(database):
    '''This takes a db connection and creates person and student tables '''
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_person_table)
        # create tasks table
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))


def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, person)
    return cur.lastrowid  # returns the row id of the cursor object, the person id


def create_student(conn, student):
    """Create a new person for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, student)
    return cur.lastrowid  # returns the row id of the cursor object, the student id


def select_student_by_name(conn, person):
    '''This Takes a connection and person tuple, searches the db, and returns the person id of the tuple
    :param conn: is a db connection
    :param person: is a first/last name person tuple
    :returns person id'''
    sql = '''SELECT id
             FROM person
             WHERE firstname=?
             AND lastname=?'''
    cur = conn.cursor()
    print(f'{person[0]} {person[1]}')
    cur.execute(sql, person)
    result = [r[0] for r in cur.fetchall()]
    return str(result).strip('[]')


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")

    rows = cur.fetchall()

    return rows  # return the rows


def select_all_students(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute('''
                SELECT p.id, p.firstname, p.lastname, s.major, s.begin_date
                FROM student s
                INNER JOIN person p ON p.id = s.id
                ''')

    rows = cur.fetchall()
    # result = [r[0] for r in cur.fetchall()]

    return rows  # return the rows


if __name__ == '__main__':
    # create_tables("pythonsqlite.db")
    #
    # conn = create_connection("dbguiassignment.db")
    # with conn:
    #     person = ('Mob', 'Thomas')
    #     person_id = create_person(conn, person)
    #
    #     student = (person_id, 'Songwriting', '2000-01-01')
    #     student_id = create_student(conn, student)

    # conn = create_connection('dbguiassignment.db')
    # with conn:
    #     rows = select_all_persons(conn)
    #     for row in rows:
    #         print(row)

    conn = create_connection("dbguiassignment.db")
    with conn:
        rows = select_all_students(conn)
        for row in rows:
            print(row)
