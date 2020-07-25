import psycopg2
from flask import Flask, render_template, redirect, url_for
from connect_to_database import connect, close_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title='Tom Hanks')

if __name__ == '__main__':
    app.run()
