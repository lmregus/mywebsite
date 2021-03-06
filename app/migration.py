from flask_migrate import Manager
from flask_migrate import Migrate
from flask_migrate import MigrateCommand

from server import app
from server import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models.code_snippet import CodeSnippet
from models.skill import Skill
from models.job import Job
from models.education import Degree
from models.site_user import SiteUser
from models.blog import Post


if __name__ == '__main__':
    manager.run()
