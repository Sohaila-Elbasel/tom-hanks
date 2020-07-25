from connect_to_database import connect, close_connection
import csv
import os

def create_table():
    try:
        (cursor, connection) = connect()
        print('connection is ok')
        create_table = '''CREATE TABLE movies(
                        id SERIAL PRIMARY KEY,
                        name VARCHAR NOT NULL,
                        pic_url VARCHAR NOT NULL,
                        year VARCHAR NOT NULL,
                        genre VARCHAR NOT NULL,
                        rate VARCHAR NOT NULL,
                        story TEXT
        );'''
        cursor.execute(create_table)
        connection.commit()
        print("table is created")
        close_connection(cursor, connection)


    except Exception as error:
        print(error)

def import_data():
    try:
        (cursor, connection) = connect()
        print('connection is ok')
        f = open('movies.csv')
        file = csv.reader(f)
        insert_data = "INSERT INTO movies (name, pic_url, year, genre, rate, story) VALUES (%s, %s, %s, %s, %s, %s)"
        for name, pic_url, year, genre, rate, story in file:
            cursor.execute(insert_data, (name, pic_url, year, genre, rate, story))

        connection.commit()
        close_connection(cursor, connection)
        print('data is inserted to database')

    except Exception as error:
        print(error)

def test_query():
    try:
        (cursor, connection) = connect()
        print('connection is ok')

        query = "SELECT * FROM movies"
        cursor.execute(query)
        print(cursor.fetchone())
        close_connection(cursor, connection)

    except Exception as error:
        print(error)

test_query()
