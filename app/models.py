#author Delika Pratiwi - Delikapratiwi@gmail.com

from datetime import datetime
from app import db

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(120), index=True, unique=True)
    status = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return '<News {}>'.format(self.title)

    def __init__(self, title, description, status):
        self.title = title
        self.description = description
        self.status = status

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    news_id = db.Column(db.Integer, db.ForeignKey('news.id'))

    def __repr__(self):
        return '<Topic {}>'.format(self.body)

    def __init__(self, name, news_id):
        self.name = name
        self.news_id = news_id