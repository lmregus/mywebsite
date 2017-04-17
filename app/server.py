import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

login_manager = LoginManager()
app = Flask(__name__)
db = SQLAlchemy(app)

if os.environ.get('HEROKU'):
    app.config.from_object('config.ProductionConfig')
else:
    app.config.from_object('config.DevelopmentConfig')

login_manager.init_app(app)
root = os.path.abspath(os.path.dirname(__file__))
