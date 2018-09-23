# app/models/region.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from .. import db

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Region(db.Model):
    '''Создаёт модель Региона'''
    __tablename__ = 'regions'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    extra = db.Column(db.String(50))

    citizens = db.relationship('User', backref='region', lazy='dynamic')
    cities = db.relationship('City', backref='region', lazy='dynamic')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extra = self.title

    def __repr__(self):
        return '<Region - {}>'.format(self.title)

