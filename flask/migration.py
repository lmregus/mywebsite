from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from server import app, db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from models.demo_model import DemoModel
from models.account import Account
from models.token import Token
from models.account_log import AccountLog
from models.more_secure import MoreSecure
from models.key import Key
from models.tiny import Editable

if __name__ == '__main__':
    manager.run()
