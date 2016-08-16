import os
try:
    from local_db_creds import *
except ImportError:
    pass


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret key'

class ProductionConfig(Config):
    #DATABASE_URI = 'postgres://username:password@localhost:5432/database'
    SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@{2}:5432/{3}'.format(os.environ.get('HEROKU_DB_USER'), os.environ.get('HEROKU_DB_PASS'), os.environ.get('HEROKU_DB_HOST'), os.environ.get('HEROKU_DB_NAME'))
    DATABASE_URI = SQLALCHEMY_DATABASE_URI

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://{0}:{1}@{2}:5432/{3}'.format(HEROKU_DB_USER, HEROKU_DB_PASS, HEROKU_DB_HOST, HEROKU_DB_NAME)
    DATABASE_URI = SQLALCHEMY_DATABASE_URI

#class TestingConfig(DevelopmentConfig):
#    TESTING = True
#    DATABASE_URI = 'postgres://postgres_test_user:pg_tst_pw@localhost:5432/postgres_test_db'
