from flask import Flask, request, jsonify, render_template, session, redirect, flash, url_for
from flask_mysqldb import MySQL
from os import urandom
from yaml import load, FullLoader
from werkzeug.security import generate_password_hash as gen, check_password_hash as check

app = Flask(__name__)
mysql = MySQL(app)

# MySQL Configuration
db_keeps = load(open('data.yaml'), Loader=FullLoader)
app.config['MYSQL_HOST'] = db_keeps['mysql_host']
app.config['MYSQL_USER'] = db_keeps['mysql_user']
app.config['MYSQL_PASSWORD'] = db_keeps['mysql_password']
app.config['MYSQL_DB'] = db_keeps['mysql_db']
app.config['SECRET_KEY'] = urandom(24)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/user/register/', methods=['GET', 'POST'])
def reg_user():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        district = form['district']
        email = form['email']
        password = gen(form['password'])
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, email, district, password) VALUES(%s, %s, %s, %s);", (name, email, district, password))
        mysql.connection.commit()
        cur.close()
        flash("Registered Successfully! You can now log in", "success")
        return redirect('/user/login/')
    return render_template('register_user.html')

@app.route('/professional/register/', methods=['GET', 'POST'])
def reg_prof():
    if request.method == 'POST':
        form = request.form
        name = form['name']
        district = form['district']
        email = form['email']
        password = gen(form['password'])
        domain =  form['domain']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO professional(name, email, domain, district, password) VALUE(%s, %s, %s, %s, %s);", (name, email, domain, district, password))
        mysql.connection.commit()
        cur.close()
        flash("Registered Successfully! You can now log in", "success")
        return redirect('/professional/login/')        
    return render_template('register_prof.html')

@app.route('/user/login/', methods=['GET', 'POST'])
def login_user():
    return render_template('login.html')

@app.route('/professional/login/', methods=['GET', 'POST'])
def login_prof():
    return render_template('login.html')

@app.route('/domain/<domain>')
def domain(domain):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issues WHERE domain='{}';".format(domain))
    domain = cur.fetchall()
    return render_template('domain.html', domain=domain)

@app.route('/issues/new/', methods=['GET', 'POST'])
def new_issue():
    if request.method == 'POST':
        form = request.form
        domain = form['domain']
        complaint = form['complaint']
        link = form['link']
        name = session['fullname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO issue(domain, complaint, link, name) VALUES(%s, %s, %s, %s);", (domain, complaint, link, name))
        mysql.connection.commit()
        cur.close()
        flash("Issue Posted Successfully", "success")
        return redirect('/home/')
    return render_template('new_issue.html')

@app.route('/issues/<int:id>/')
def issue_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue WHERE id={}".format(id))
    issue = cur.fetchone()


@app.route('/blogs/new/')
def new_blog():
    pass

@app.route('/profile/me/')
def me():
    pass


if __name__ == '__main__':
    app.run(debug=True)