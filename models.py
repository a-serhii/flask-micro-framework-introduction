from datetime import datetime
from app import db
from sqlalchemy import desc


class Bookmark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    description = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    @staticmethod
    def newest(num):
        return Bookmark.query.order_by(desc(Bookmark.date)).limit(num)


    def __repr__(self):
        return '<Bookmark "{}" : "{}">'.format(self.description, self.url)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(50), unique=True)
    bookmarks = db.relationship('Bookmark', backref='user', lazy='dynamic')


    def __repr__(self):
        return 'User %r' % self.username