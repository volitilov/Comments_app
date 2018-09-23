# ex package

# инициализирует и получает необходимые данные для работы пакета

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import Blueprint

from .data import page_titles

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

comment = Blueprint(name='comment', import_name=__name__)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from . import requests_get, requests_post