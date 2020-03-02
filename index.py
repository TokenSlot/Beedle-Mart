from flask import Flask, session, render_template, request, redirect, url_for
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bE2xieW16swUOGQ95CJJyg'


dbname = 'beedle_db'
user = 'admin'
password = '1234'
conn = psycopg2.connect(database=dbname, user=user, password=password)

@app.route('/')
def index():
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    query = "select * from users"
    cursor.execute(query)
    users = cursor.fetchall()

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True

    return render_template('index.html', users=users, username=username, isSessionOn=isSessionOn)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/sign-up')
def signup():
    return redirect("/")

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/sign-in')
def signin():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)