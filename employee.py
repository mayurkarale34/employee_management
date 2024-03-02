from flask import Flask, render_template, redirect, request, jsonify

from sqlalchemy import create_engine, text
from config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME, DATABASE_NAME

def init_engine(app):
    app._engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME + '?charset=utf8')

app = Flask(__name__)
app.debug = True
init_engine(app)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    user_name = "Admin"
    return render_template('home.html', username = user_name)


@app.route('/validate_login', methods = ['POST'])
def validate_login():
    data = dict(request.form)
    user_name = data['username']
    password = data['password']
    if user_name.upper() == 'ADMIN' and password.upper()=='ADMIN':
        return jsonify({"status" : True})
    else:
        return jsonify({"status" : False})
    
@app.route('/empmanagement')
def empmanagement():
    user_name = "Admin"
    return render_template('empmanagement.html', username = user_name)
app.run(port = 5000)