from datetime import datetime
from job_func import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search_keyword = db.Column(db.String(100), nullable=False)
    search_location = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_posted = db.Column(db.String(100), nullable=True)
    hiring_organisation = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Job('{self.title}')"

