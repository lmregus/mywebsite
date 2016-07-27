import os
from flask import Flask
from server import app

from controllers import general
from controllers import code_snippet

if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 3733
    )
