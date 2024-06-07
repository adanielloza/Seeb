from utils.database import db
from flask_login import UserMixin

class Status(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    status_description = db.Column(db.String(50))
    time = db.Column(db.Integer)
    
    def serialize(self):
        return {
            "id": self.id,
            "status_description": self.status_description,
            "time": self.time
        }