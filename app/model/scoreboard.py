from email.policy import default
from app import db
from datetime import datetime


class Score(db.Model):
    __tablename__ = "scoreboard"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name} - {self.score}/10"
