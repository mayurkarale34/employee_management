from flask import Flask, render_template, redirect, flash, request, jsonify, session

from sqlalchemy import create_engine, text
from config import DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOSTNAME, DATABASE_NAME
from datetime import datetime
import random
import string

from flask_caching import Cache
from flask_cors import CORS

def init_engine(app):
    app._engine = create_engine('mysql://' + DATABASE_USERNAME + ':' + DATABASE_PASSWORD + '@' + DATABASE_HOSTNAME + '/' + DATABASE_NAME + '?charset=utf8')

def set_greetings():
    """
    Generate a time-based greeting message.

    Parameters:
        name (str): The name of the person to greet.

    Returns:
        str: A time-based greeting message including the provided name.
    """
    current_time = datetime.now()
    hour = current_time.hour

    if 5 <= hour < 12:
        return f"Good Morning"
    elif 12 <= hour < 18:
        return f"Good Afternoon"
    else:
        return f"Good Evening"

app = Flask(__name__)
CORS(app, origins="*")
app.secret_key = '123456'
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
app.debug = True
init_engine(app)