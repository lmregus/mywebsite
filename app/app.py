import os
from server import app

from controllers import general
from controllers import code_snippet
from controllers import skill


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 3733
    )
