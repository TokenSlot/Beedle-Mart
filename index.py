from flask import Flask, session, render_template, request, redirect, url_for
import psycopg2, hashlib
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bE2xieW16swUOGQ95CJJyg'


dbname = 'beedle_db'
user = 'admin'
password = '1234'
conn = psycopg2.connect(database=dbname, user=user, password=password)

@app.route('/')
def index():
    # cursor = conn.cursor(cursor_factory = RealDictCursor)
    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True

    return render_template('index.html', username=username, isSessionOn=isSessionOn)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not session.get('USERNAME') is None:
        return redirect('/')
    return render_template('login.html')

@app.route('/sign-in', methods=['POST'])
def signin():

    username = request.form['username']
    password = request.form['password']
    encryptedPass = hashlib.md5(password.encode())

    cursor = conn.cursor()

    query = "SELECT user_id FROM users WHERE username=%s AND password=%s"
    data = (username, encryptedPass.hexdigest())
    cursor.execute(query, data)
    userId = cursor.fetchone()

    if userId is None:
        error = "Invalid username or password."
        return render_template('login.html', error=error)

    session['ID'] = userId
    session['USERNAME'] = username
    return redirect("/")

@app.route('/register', methods=['GET','POST'])
def register():
    if not session.get('USERNAME') is None:
        return redirect('/')
    return render_template('register.html')

@app.route('/sign-up', methods=['POST'])
def signup():
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    contactNo = request.form['contactNo']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    username = request.form['username']
    password = request.form['password']
    encryptedPass = hashlib.md5(password.encode())
    address = request.form['address']
    address2 = request.form['address2']
    city = request.form['city']
    country = request.form['country']
    postalCode = request.form['postalCode']

    cursor = conn.cursor()

    query = "SELECT username FROM users WHERE username=%s"
    data = [username]
    cursor.execute(query, data)
    num_rows = cursor.fetchall()

    if len(num_rows) > 0:
        error = 'Username already exist.'
        return render_template('register.html', error=error)


    query = "SELECT email FROM users WHERE email=%s"
    data = [email]
    cursor.execute(query, data)
    num_rows = cursor.fetchall()

    if len(num_rows) > 0:
        error = 'Email already registered.'
        return render_template('register.html', error=error)


    query = '''INSERT INTO users
            (first_name, last_name, email, contact_no,
            gender, birthdate, username, password)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
    data = (fname, lname, email, contactNo, gender, birthdate, username, encryptedPass.hexdigest())
    cursor.execute(query, data)
    conn.commit()

    query = "SELECT user_id FROM users WHERE username=%s AND password=%s"
    data = (username, encryptedPass.hexdigest())
    cursor.execute(query, data)
    userId = cursor.fetchone()

    query = "SELECT user_id FROM users WHERE username=%s AND password=%s"
    data = (username, encryptedPass.hexdigest())
    cursor.execute(query, data)
    userId = cursor.fetchone()

    query = '''INSERT INTO addresses
            (user_id, address, address2, city, postal_code, country_code)
            VALUES (%s, %s, %s, %s, %s, %s)'''
    data = (userId, address, address2, city, postalCode, country)
    cursor.execute(query, data)
    conn.commit()

    cursor.close()

    session['ID'] = userId
    session['USERNAME'] = username
    return redirect("/")

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect("/")

@app.route('/404')
def error404():
    return render_template('404.html')

@app.route('/profile/<profile_user>', methods=['GET', 'POST'])
def profile(profile_user):

    cursor = conn.cursor()
    query = "SELECT user_id FROM users WHERE username=%s"
    data = [profile_user]
    cursor.execute(query, data)
    userId = cursor.fetchone()

    if userId is None:
        return redirect('/404')

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('profile.html', profile_user=profile_user,username=username, isSessionOn=isSessionOn)

@app.route('/shop/<profile_user>', methods=['GET', 'POST'])
def shop(profile_user):

    cursor = conn.cursor()
    query = "SELECT user_id FROM users WHERE username=%s"
    data = [profile_user]
    cursor.execute(query, data)
    userId = cursor.fetchone()

    if userId is None:
        return redirect('/404')

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('shop.html', profile_user=profile_user,username=username, isSessionOn=isSessionOn)


if __name__ == "__main__":
    app.run(debug=True)