import psycopg2
from flask import Flask, render_template, redirect, url_for
from connect_to_database import connect, close_connection

app = Flask(__name__)

@app.route('/')
def home():
    try:
        data = []
        (cursor, connection) = connect()
        query = "SELECT name, pic_url, year, genre, rate FROM movies"
        cursor.execute(query)
        result = cursor.fetchmany(4)
        for row in result:
            data.append(row)
        close_connection(cursor, connection)

    except Exception as error:
        print(error)
    return render_template('home.html', title='Tom Hanks', data = data)

if __name__ == '__main__':
    app.run()
