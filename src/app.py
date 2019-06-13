_author_ = 'Ta-Seen Junaid'

from src.models.user import User
from src.common.database import Database
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "junaid"

@app.route('/')

def hello_method():
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/login', methods = ['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)

    return render_template("profile.html", email=session['email'])




if __name__=='__main__':
    app.debug = True
    app.run(port = 4996)