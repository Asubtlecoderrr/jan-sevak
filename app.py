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
    if request.method == 'POST':
        form = request.form
        email = form['email']
        password = form['password']
        cur = mysql.connection.cursor()
        usercheck = cur.execute("SELECT * FROM user WHERE email=%s", ([email]))
        if usercheck > 0:
            user = cur.fetchone()
            checker = check(user[-2], password)
            if checker:
                session['logged_in'] = True
                session['full_name'] = user[1]
                session['district'] = user[3]
                session['id'] = user[0]
                flash(f"Welcome {session['full_name']}!! Your Login is Successful", 'success')
            else:
                cur.close()
                flash('Wrong Password!! Please Check Again.', 'danger')
                return render_template('login.html')
        else:
            cur.close()
            flash('User Does Not Exist!! Please Enter Valid Username.', 'danger')
            return render_template('login.html')
        cur.close()
        return redirect('/home/')
    return render_template('login.html', role='user')

@app.route('/professional/login/', methods=['GET', 'POST'])
def login_prof():
    return render_template('login.html', role='professional')

@app.route('/domain/<domain>/')
def domain(domain):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue WHERE domain='{}';".format(domain))
    issues = cur.fetchall()
    return render_template('issue.html', issues=issues, domain=domain)

@app.route('/issues/new/', methods=['GET', 'POST'])
def new_issue():
    if request.method == 'POST':
        form = request.form
        domain = form['domain']
        complaint = form['complaint']
        link = form['link']
        name = session['full_name']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO issue(domain, complaint, link, name) VALUES(%s, %s, %s, %s);", (domain, complaint, link, name))
        mysql.connection.commit()
        cur.close()
        flash("Issue Posted Successfully", "success")
        return redirect('/home/')
    return render_template('new.html')

@app.route('/issues/<int:id>/')
def issue_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue WHERE id={}".format(id))
    issue = cur.fetchone()
    return render_template('issueinfo.html', issue=issue)

@app.route('/issues/<int:id>/solved/')
def solved(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue WHERE id={};".format(id))
    res = cur.fetchone()
    cur.execute("DELETE FROM issue WHERE id={};".format(id))
    mysql.connection.commit()
    cur.execute("INSERT INTO solved(domain, complaint, link, name) VALUES(%s, %s, %s, %s);", (res[1], res[2], res[3], res[-1]))
    mysql.connection.commit()
    print(cur.fetchone())
    cur.close()
    flash("Issue Marked as Resolved", "success")
    return redirect('/home/')

@app.route('/blogs/')
def blog():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM blog;")
    blogs = cur.fetchall()
    return render_template('blog.html', blogs=blogs)

@app.route('/blogs/<int:id>/')
def blog_id(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM issue WHERE id={}".format(id))
    issue = cur.fetchone()
    return render_template('bloginfo.html')

@app.route('/my-issues/')
def me():
    cur = mysql.connection.cursor()
    q = cur.execute("SELECT * FROM issue WHERE name='{}';".format(session['full_name']))
    if q > 0:
        my_issues = cur.fetchall()
        return render_template('myissues.html', issues=my_issues)
    return render_template('myissues.html', issues=None)

if __name__ == '__main__':
    app.run(debug=True)