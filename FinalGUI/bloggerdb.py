"""
Author: Alex Alvarado
Date: 11-29-20
Program: bloggerdb.py
Description: The database where the posts and the bloggers will be stored!
"""

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

    sql_create_blogger_table = """ CREATE TABLE IF NOT EXISTS blogger (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL,
                                        date text NOT NULL
                                    ); """

    sql_create_post_table = """ CREATE TABLE IF NOT EXISTS post (   
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL,
                                        post text NOT NULL,
                                        FOREIGN KEY (id) REFERENCES blogger (id)
                                    ); """

    # create a database connection
    conn = create_connection(database)
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_blogger_table)
        create_table(conn, sql_create_post_table)
    else:
        print("Unable to connect to " + str(database))

def create_post(conn, post):

    sql = ''' INSERT INTO post(firstname,lastname,post)
              VALUES(?,?,?) '''

    cur = conn.cursor()  # cursor object
    cur.execute(sql, post)

    return cur.lastrowid



def create_blogger(conn, blogger):
    """Create a new person for table
    :param conn:
    :param blogger:
    :return: person id
    """
    sql = ''' INSERT INTO blogger(firstname,lastname,date)
              VALUES(?,?,?) '''
    cur = conn.cursor()  # cursor object
    cur.execute(sql, blogger)
    return cur.lastrowid # returns the row id of the cursor object, the person id

def select_all_bloggers(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM blogger")

    rows = cur.fetchall()

    return rows # return the rows

def select_all_posts(conn):

    cur = conn.cursor()
    cur.execute("SELECT * FROM post")
    rows = cur.fetchall()
    return rows # return the rows


def delete_post_table(conn):
    sql = 'DELETE FROM post'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def delete_blogger_table(conn):
    sql = 'DELETE FROM blogger'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def users_posts(conn, firstname):
    sql = 'SELECT * FROM post WHERE firstname=?'
    cur = conn.cursor()
    cur.execute(sql, (firstname,))
    user_posts = cur.fetchall()
    conn.commit()
    return user_posts

if __name__ == '__main__':
    conn = create_connection("bloggerdb.db")
    create_tables("bloggerdb.db")




