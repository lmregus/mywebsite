import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object('config.DevelopmentConfig')

root = os.path.abspath(os.path.dirname(__file__))
