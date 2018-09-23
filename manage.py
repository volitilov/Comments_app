#!.venv/bin/python3

# manage.py

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, click

from app import create_app
from app import db as database

from app.utils import addFake_data
from app.models.user import User
from app.models.comment import Comment
from app.models.region import Region
from app.models.city import City

from flask_migrate import MigrateCommand, Migrate
from dotenv import load_dotenv


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

# загрузка переменных необходимых для работы приложения в виртуальное
# окружение приложения
load_dotenv()


app = create_app(os.environ.get('APP_ENV', default='default'))
migrate = Migrate(app, database)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
# команды командной строки

# flask db
@app.cli.command()
def db():
    '''Выполняет миграции базы данных'''
    return MigrateCommand


# flask add_data
@app.cli.command()
def add_data():
    '''Выполняет комманду добавления фейковых данных'''
    addFake_data()


# flask shell
@app.shell_context_processor
def make_shell_context():
    '''Запускает shell со сконфигурированым контекстом'''
    return dict(app=app, db=database, User=User, Comment=Comment, 
        City=City, Region=Region)


# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

if __name__ == '__main__':
    app.run()
