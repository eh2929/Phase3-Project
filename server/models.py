from config import db
from flask_sqlalchemy import SQLAlchemy


class Job_application(db.Model):
    __tablename__ = "Job Application"

    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    status = db.Column(db.String)
    notes = db.Column(db.String)
    date_applied = db.Column(db.Date)

    company_id = db.Column(db.Integer, db.ForeignKey("Companies.id"))
    company = db.relationship("Companies", backref="job_applications")

    def __repr__(self):
        return f"Name: {self.job_title}"


class Companies(db.Model):
    __tablename__ = "Companies"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    industry = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    notes = db.Column(db.String)

    def __repr__(self):
        return f"Name: {self.name}"
