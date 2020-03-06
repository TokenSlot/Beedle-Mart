from flask import Flask, session, render_template, request, redirect, url_for
import psycopg2, hashlib
from psycopg2.extras import RealDictCursor

import os, math, time

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bE2xieW16swUOGQ95CJJyg'


dbname = 'beedle_db'
user = 'admin'
password = '1234'
conn = psycopg2.connect(database=dbname, user=user, password=password)

@app.route('/')
def index():
    cursor = conn.cursor(cursor_factory = RealDictCursor)
    query = '''select * from
            (select distinct * from products) products
            ORDER BY random() limit 3;
            '''
    cursor.execute(query)
    feats = cursor.fetchall()

    query = '''select * from
            (select distinct * from products) products
            ORDER BY random() limit 3;
            '''
    cursor.execute(query)
    tops = cursor.fetchall()

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True

    return render_template('index.html', feats=feats, tops=tops, username=username, isSessionOn=isSessionOn)

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

    userId = session.get('ID')

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT user_id FROM users WHERE username=%s"
    data = [profile_user]
    cursor.execute(query, data)
    owner = cursor.fetchone()

    if owner is None:
        return redirect('/404')

    query = "SELECT * FROM products WHERE user_id=%s"
    data = [owner['user_id']]
    cursor.execute(query, data)
    products = cursor.fetchall()

    

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('shop.html', profile_user=profile_user, products=products,username=username, isSessionOn=isSessionOn)

@app.route('/browse', methods=['GET', 'POST'])
def browse():

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT * FROM products"
    cursor.execute(query)
    products = cursor.fetchall()

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('browse.html', products=products,username=username, isSessionOn=isSessionOn)

@app.route('/search', methods=['GET', 'POST'])
def search():
    keyword = request.form['keyword']
    return redirect('/browse/'+keyword)

@app.route('/browse/<keyword>', methods=['GET', 'POST'])
def browseSearch(keyword):
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    data = keyword.lower()
    query = "SELECT * FROM products WHERE lower(product_name) LIKE '%"+data+"%'"
    cursor.execute(query)
    products = cursor.fetchall()

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('browse.html', products=products,username=username, isSessionOn=isSessionOn)

@app.route('/product/<id>', methods=['GET', 'POST'])
def product(id):

    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT * FROM products WHERE product_id = %s"
    data = [id]
    cursor.execute(query, data)
    product = cursor.fetchone()

    userId = product['user_id']

    query = "SELECT username FROM users WHERE user_id = %s"
    data = [userId]
    cursor.execute(query, data)
    owner = cursor.fetchone()   

    username = ''
    isSessionOn = False
    if not session.get('USERNAME') is None:
        username = session.get("USERNAME")
        isSessionOn = True
    return render_template('product.html', product=product, owner=owner, username=username, isSessionOn=isSessionOn)



app.config["IMAGE_UPLOADS"] = 'static\\img'


@app.route('/add/item', methods=['GET', 'POST'])
def addItem():

    if request.method == "POST":

        userId = session.get('ID')
        productName = request.form['productName']

        image = request.files['productImg']
        image_name = str(time.time())+'_'+session.get('USERNAME')+'_'+image.filename
        image.save(os.path.join(app.config["IMAGE_UPLOADS"], image_name))
        productImg = image_name

        productInfo = request.form['productInfo']
        origPrice = float(request.form['origPrice'])
        discPrice = float(request.form['discPrice'])

        if origPrice == discPrice or discPrice == '':
            price = origPrice
            discount = '0'
        else:
            price = discPrice
            disc_comp = math.ceil(100-((discPrice/origPrice)*100))
            discount = str(disc_comp)

        stock = request.form['stock']

        cursor = conn.cursor()
        query = '''INSERT INTO products
                (user_id, product_name, product_img, product_info, price, stock, orig_price, discount) VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s)'''
        data = (userId, productName, productImg, productInfo, str(price), stock, str(origPrice), discount)
        cursor.execute(query, data)
        conn.commit()

    return redirect(url_for('shop', profile_user=session.get('USERNAME')))



if __name__ == "__main__":
    app.run(debug=True)