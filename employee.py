from flask import Flask, render_template, redirect, request, jsonify

from sqlalchemy import create_engine, text
from config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME, DATABASE_NAME

def init_engine(app):
    app._engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME + '?charset=utf8')

app = Flask(__name__)
app.debug = True
init_engine(app)
app.run(port = 5000)