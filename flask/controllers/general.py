from server import app

from flask import render_template
from flask import request
from flask import redirect


@app.route('/')
def index():
    return render_template('index.html')

