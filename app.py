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


@app.route('/db_create')
def create_table():
    conn = psycopg2.connect("postgresql://flask_piping_render_db_user:8klJtTe2LBKnf4r4M5dfNAPZP8emX7gY@dpg-cql9u3t6l47c73ani3pg-a/flask_piping_render_db")
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'

@app.route('/db_insert')
def insert_data():
    conn = psycopg2.connect("postgresql://flask_piping_render_db_user:8klJtTe2LBKnf4r4M5dfNAPZP8emX7gY@dpg-cql9u3t6l47c73ani3pg-a/flask_piping_render_db")
    cur = conn.cursor()
    cur.execute('''
    INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Populated'

@app.route('/db_select')
def select_data():
    conn = psycopg2.connect("postgresql://flask_piping_render_db_user:8klJtTe2LBKnf4r4M5dfNAPZP8emX7gY@dpg-cql9u3t6l47c73ani3pg-a/flask_piping_render_db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response = ''
    response += '<table>'
    for record in records:
        response += '<tr>'
        for field in record:
            response += '<td>' + str(field) + '</td>'
        response += '</tr>'
    response += '</table>'
    return response


@app.route('/db_drop')
def drop_all():
    conn = psycopg2.connect("postgresql://flask_piping_render_db_user:8klJtTe2LBKnf4r4M5dfNAPZP8emX7gY@dpg-cql9u3t6l47c73ani3pg-a/flask_piping_render_db")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Dropped'

