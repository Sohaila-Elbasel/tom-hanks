import psycopg2
from configparser import ConfigParser

def config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()

    parser.read(filename)
    db = {}

    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in the {filename} file')

    return db

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
