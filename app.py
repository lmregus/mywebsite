import os
from flask.server import app

from flask.controllers import general
from flask.controllers import code_snippet

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 3733
    )
