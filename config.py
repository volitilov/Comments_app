# config.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os
from dotenv import load_dotenv

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', default=os.urandom(32))
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY', default=os.urandom(32))

    WTF_CSRF_ENABLED = True

    SQLALCHEMY_TRACK_MODIFICATIONS = False


    @staticmethod
    def init_app(app): pass



class DevelopmentConfig(Config):
    FLASK_DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 
        default='sqlite:///' + os.path.join(basedir, 'data_dev.sqlite'))




class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 
        default='sqlite:///' + os.path.join(basedir, 'data.sqlite'))




class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 
        'data_test.sqlite')



# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,

    'default': DevelopmentConfig
}