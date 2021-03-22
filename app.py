from flask import Flask, request, jsonify, render_template, session, redirect, flash
from flask_mysqldb import MySQL
from os import urandom
from yaml import load, FullLoader

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
    return 'This is the beginning of a revolution'

@app.route('/register/')
def register():
    pass

@app.route('/login/')
def login():
    return render_template('login.html')

@app.route('/banking/')
def banking():
    pass

@app.route('/farming/')
def farming():
    pass

@app.route('/healthcare/')
def healthcare():
    pass

@app.route('/govt-schemes/')
def schemes():
    pass

@app.route('/miscellaneous/')
def misc():
    pass

@app.route('/blogs/')
def blogs():
    pass

@app.route('/issues/new/')
def new_issue():
    pass

@app.route('/blogs/new/')
def new_blog():
    pass

@app.route('/profile/me/')
def me():
    pass


if __name__ == '__main__':
    app.run(debug=True)