from server import db
from server import app


class Job(db.Model):
    __tablename__="job"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    time_period = db.Column(db.String(64))
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
        job.title = data['title']
        job.time_period = data['time_period']
        job.company = data['company']
        job.description = data['description']
        db.session.add(job)
        db.session.commit()
        return job

    def update(self, data):
        job = Job.query.get(data['id'])
        job.title = data['title']
        job.time_period = data['time_period']
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
