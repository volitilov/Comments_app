# auth/forms.py

# Файл для работы с форммами

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask_wtf import FlaskForm
from wtforms import (
    StringField, SelectField, TextAreaField, IntegerField
)
from wtforms.validators import Required, Email, Length, Regexp

from ..models.region import Region

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class AddComment_form(FlaskForm):
    '''Инициализирует форму для добавления комментария'''
    first_name = StringField(label='Имя', validators=[
        Length(min=3, max=64, message='Имя не должено быть меньше 3 и больше 64 символов')])

    last_name = StringField(label='Фамилия', validators=[
        Length(min=3, max=64, message='Фамилия не должена быть меньше 3 и больше 64 символов')])

    middle_name = StringField(label='Отчество')
    
    email = StringField(label='Email', validators=[Email(message='Введите email')])

    phone = StringField(label='Телефон')
    region = SelectField(label='Регион')
    city = SelectField(label='Город')
    
    comment = TextAreaField(label='Комментарий', validators=[
        Length(min=10, max=5000, message='Комментарий не должен быть меньше 10 и больше 5000 символов')])

        