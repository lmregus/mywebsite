from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from server import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models.code_snippet import CodeSnippet

if __name__ == '__main__':
    manager.run()
