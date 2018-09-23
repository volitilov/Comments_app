# app/models/comment.py

#

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from datetime import datetime
from .. import db

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class Comment(db.Model):
    '''Создаёт модель комментария'''
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __str__(self):
        return '<Comment - {}>'.format(self.id)

