class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret key'

#class ProductionConfig(Config):
#    DATABASE_URI = 'postgres://username:password@localhost:5432/database'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgres://postgres_test_user:pg_tst_pw@localhost:5432/postgres_test_db'
    DATABASE_URI = SQLALCHEMY_DATABASE_URI

class TestingConfig(DevelopmentConfig):
    TESTING = True
    DATABASE_URI = 'postgres://postgres_test_user:pg_tst_pw@localhost:5432/postgres_test_db'
