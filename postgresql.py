from connect_to_database import connect, close_connection

try:
    (cursor, connection) = connect()
    print('connection is ok')
    create_table = '''CREATE TABLE movies(
                    id SERIAL PRIMARY KEY,
                    name CHARVAR
    );'''
    cursor.execute()

except Exception as error:
    print(error)
