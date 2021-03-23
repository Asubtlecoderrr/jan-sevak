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
    if session['login'] == True:
        return redirect('/home/')
    return render_template('home.html')

@app.route('/home/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue;")
    q = cur.fetchall()
    if q > 0:
        issues = cur.fetchall()
        return render_template('index.html', issues=issues)
    else:
        issues = None
        return render_template('index.html', issues=issues)
    return render_template('index.html')

@app.route('/user/register/', methods=['GET', 'POST'])
def reg_user():
    if request.method == 'POST':
        pass
    return render_template('register.html')

@app.route('/professional/register/', methods=['GET', 'POST'])
def reg_prof():
    if request.method == 'POST':
        pass
    return render_template('register.html')

@app.route('/register/continue', methods=['GET', 'POST'])
def continue_reg():
    pass


@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/domain/<domain>')
def domain(domain):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issues WHERE domain='{}';".format(domain))
    domain = cur.fetchall()


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