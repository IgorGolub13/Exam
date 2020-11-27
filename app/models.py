



from . import db
from datetime import datetime as dt


class Audio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    class_music = db.Column(db.String(30), nullable=False)
    singer = db.Column(db.String(30), nullable=False)
    describe = db.Column(db.String(30))
    date_posted = db.Column(db.DateTime, nullable=False, default=dt.utcnow())
    length = db.Column(db.String(30), nullable=False)
    data_type = db.Column(db.String(30), nullable=False)
    rating_ball = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}'"