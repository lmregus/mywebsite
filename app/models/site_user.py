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

    def is_authenticaded(self, data):
        users = SiteUser.query.all()
        auth_user = ''
        for user in users:
            if data['name'] == user.name or data['email'] == user.email:
                if data['password'] == user.password:
                    auth_user = user
                    return True
            else:
                return False
        return False

    def get_id(self, data):
        users = SiteUser.query.all()
        for user in users:
            if data['name'] == user.name or data['email'] == user.email:
                return user.id
        return False

    def is_active(self, data):
        if is_authenticaded(data):
            return True
        return False

    def is_anonymous(self):
        return False
