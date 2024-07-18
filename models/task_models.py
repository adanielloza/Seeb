from utils.database import db
from flask_login import UserMixin

class Task(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(50))
    difficulty = db.Column(db.String(50))
    estimatetime = db.Column(db.Integer)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), default=1)
    donetime = db.Column(db.Integer, nullable=True)
    

    def serialize(self):
        return {
            "id": self.id,
            "job_id": self.job_id,
            "user_id": self.user_id,
            "description": self.description,
            "difficulty": self.difficulty,
            "estimatetime": self.estimatetime,
            "status_id": self.status_id,
            "donetime": self.donetime   
        }