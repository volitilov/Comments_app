# app/models/city.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from .. import db

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class City(db.Model):
    '''Создаёт модель города'''
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    extra = db.Column(db.String(50))

    citizens = db.relationship('User', backref='city', lazy='dynamic')
    region_id = db.Column(db.Integer, db.ForeignKey('regions.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.extra = self.title


    def __repr__(self):
        return '<City - {}>'.format(self.title)

