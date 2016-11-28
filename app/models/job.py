from server import db
from server import app

import datetime


class Job(db.Model):
    __tablename__="job"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    company = db.Column(db.String(128))
    description = db.Column(db.Text())

    def get_all(self):
        jobs = Job.query.all()
        return jobs

    def get_by_id(self, job_id):
        job = Job.query.get(job_id)
        return job

    def create(self, data):
        job = Job()
        day_s, month_s, year_s = data['start_date'].split('/')
        job.title = data['title']
        job.start_date = datetime.date(int(year_s), int(month_s), int(day_s))
        if data['end_date']:
            day_e, month_e, year_e = data['end_date'].split('/')
            job.end_date = datetime.date(int(year_e), int(month_e), int(day_e))
        else:
            job.end_date = datetime.date(int(year_s), int(month_s), int(day_s))
        job.company = data['company']
        job.description = data['description']
        db.session.add(job)
        db.session.commit()
        return job

    def update(self, data):
        job = Job.query.get(data['id'])
        day_s, month_s, year_s = data['start_date'].split('/')
        job.title = data['title']
        job.start_date = datetime.date(int(year_s), int(month_s), int(day_s))
        if data['end_date']:
            day_e, month_e, year_e = data['end_date'].split('/')
            job.end_date = datetime.date(int(year_e), int(month_e), int(day_e))
        else:
            job.end_date = datetime.date(int(year_s), int(month_s), int(day_s))
        job.company = data['company']
        job.description = data['description']
        db.session.add(job)
        db.session.commit()
        return job
    
    def delete(self, job_id):
        job = Job.query.get(data['id'])
        db.session.delete(job)
        db.sesson.commit()
        return job
