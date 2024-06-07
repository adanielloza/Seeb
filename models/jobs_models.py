from utils.database import db
from flask_login import UserMixin
from sqlalchemy import Date  # Import the Date class from the datetime module

class Job(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    initdate = db.Column(Date)
    enddate = db.Column(Date)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'initdate': self.initdate,
            'enddate': self.enddate
        }