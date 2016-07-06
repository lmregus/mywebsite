import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object('config.DevelopmentConfig')

root = os.path.abspath(os.path.dirname(__file__))
