import os
from server import app

from controllers import general
from controllers import code_snippet
from controllers import skill
from controllers import job
from controllers import education
from controllers import blog


if __name__ == '__main__':
    app.run(
        host = '0.0.0.0',
        port = 3733
    )
