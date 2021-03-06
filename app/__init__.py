# app/__init__.py

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import Flask
from config import config

# extension
from flask_sqlalchemy import SQLAlchemy

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    config[config_name].init_app(app)

    db.init_app(app)

    from .comment import comment
    app.register_blueprint(comment)

    return app
