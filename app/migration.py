from flask.ext.script import Manager
from flask.ext.migrate import Migrate
from flask.ext.migrate import MigrateCommand

from server import app
from server import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models.code_snippet import CodeSnippet
from models.skill import Skill
from models.job import Job


if __name__ == '__main__':
    manager.run()
