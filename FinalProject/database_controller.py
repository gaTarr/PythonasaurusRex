"""CIS189 Python
Author: Greg Tarr
Created: 11/30/2019"""
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
    except Error as err:
        print(err)


def create_tables(database):
    '''This takes a db connection and creates person and student tables '''
    # sql_create_anagram_table = """ CREATE TABLE IF NOT EXISTS anagrams (
    #                                     id integer PRIMARY KEY,
    #                                     anagram text NOT NULL,
    #                                     word text NOT NULL
    #                                 ); """
    sql_create_anagram_table = """ CREATE TABLE IF NOT EXISTS most_anagrams (
                                        id integer PRIMARY KEY,
                                        anagram text NOT NULL,
                                        amount text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create table
        create_table(conn, sql_create_anagram_table)
    else:
        print("Unable to connect to " + str(database))


def log_anagram_count(conn, anagram):
    """Create a new person for table
    :param conn:
    :param anagram:
    :return: anagram id
    """
    sql = ''' INSERT INTO most_anagrams(anagram, amount )
              VALUES(?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, anagram)
    return cur.lastrowid  # returns the row id of the cursor object, the anagram id


# def create_anagram(conn, anagram):
#     """Create a new person for table
#     :param conn:
#     :param anagram:
#     :return: anagram id
#     """
#     sql = ''' INSERT INTO anagrams(anagram, word)
#               VALUES(?,?) '''
#     cur = conn.cursor()  # cursor object
#     cur.execute(sql, anagram)
#     return cur.lastrowid  # returns the row id of the cursor object, the anagram id
#
#
# def select_words_by_anagram(conn, anagram):
#     '''This Takes
#     :param conn: is a db connection
#     :param anagram:
#     :returns person id'''
#     sql = '''SELECT word
#              FROM anagrams
#              WHERE anagram=?'''
#     cur = conn.cursor()
#     print(anagram)
#     cur.execute(sql, [anagram])
#     # result = [r[0] for r in cur.fetchall()]
#     # return str(result).strip('[]')
#     rows = cur.fetchall()
#     return rows
#
#
# def select_all_anagrams(conn):
#     """Query all rows of anagrams table
#     :param conn: the connection object
#     :return:
#     """
#     cur = conn.cursor()
#     cur.execute("SELECT * FROM anagrams")
#
#     rows = cur.fetchall()
#
#     return rows  # return the rows
