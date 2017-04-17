from server import db
from server import app

import bcrypt


class SiteUser(db.Model):
    __tablename__="site_user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(256))
    password = db.Column(db.String(256))

    def get_all(self):
        users = SiteUser.query.all()
        return users

    def get_by_id(self, user_id):
        user = SiteUser.query.get(user_id)
        return user

    def create(self, data):
        user = SiteUser()
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, data):
        user = SiteUser.query.get(data['id'])
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user_id):
        user = SiteUser.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user
