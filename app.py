import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Lerena in 3308!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flask_piping_render_db_user:8klJtTe2LBKnf4r4M5dfNAPZP8emX7gY@dpg-cql9u3t6l47c73ani3pg-a/flask_piping_render_db")
    conn.close()
    return 'Database connection successful!'

