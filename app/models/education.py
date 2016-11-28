from server import db
from server import app

import datetime

class Degree(db.Model):
    __tablename__="education"
    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.String(128))
    _type = db.Column(db.String(64))
    title = db.Column(db.String(128))
    description = db.Column(db.Text())
    date = db.Column(db.DateTime)

    def get_all(self):
        degrees = Degree.query.all()
        return degrees

    def get_by_id(self, degree_id):
        degree = Degree.query.get(degree_id)
        return degree

    def create(self, data):
        degree = Degree()
        day, month, year = data['date'].split('/')
        degree.title = data['title']
        degree.school = data['school']
        degree._type = data['type']
        degree.description = data['description']
        degree.date = datetime.date(int(year), int(month), int(day))
        db.session.add(degree)
        db.session.commit()
        return degree

    def update(self, data):
        degree = Degree.query.get(data['id'])
        day, month, year = data['date'].split('/')
        degree.title = data['title']
        degree.school = data['school']
        degree._type = data['type']
        degree.description = data['description']
        degree.date = datetime.date(int(year), int(month), int(day))
        db.session.add(degree)
        db.session.commit()
        return degree

    def delete(self, degree_id):
        degree = Degree.query.get(degree_id)
        db.session.delete(degree)
        db.session.commit()
        return degree
