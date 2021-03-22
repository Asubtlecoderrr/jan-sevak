from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

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