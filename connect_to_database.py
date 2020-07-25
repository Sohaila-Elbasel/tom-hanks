import psycopg2
from config import config

def close_connection(cursor, connection):
    try:
        cursor.close()
        connection.close()
    except:
        raise('Connection Can\'t be closed')

def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
        cursor = connection.cursor()
        return (cursor, connection)

    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
