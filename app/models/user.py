# app/models/user.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from datetime import datetime

from .. import db

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class User(db.Model):
    '''Создаёт пользователей'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    middle_name = db.Column(db.String(64), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow()) 
    phone = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), unique=True, index=True, nullable=False)
   
    comments = db.relationship('Comment', backref='author', lazy='dynamic')
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    def __repr__(self):
        return '<User - {}>'.format(self.email)
