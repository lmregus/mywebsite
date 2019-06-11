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

    def get_by_username(self, username):
        user = SiteUser.query.all()
        for u in user:
            if u.name == username:
                return u
        return false

    def create(self, data):
        user = SiteUser()
        user.name = data['name']
        user.email = data['email']
        user.password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, data):
        user = SiteUser.query.get(data['id'])
        user.name = data['name']
        user.email = data['email']
        user.password = bcrypt.hashpw(data['password'].encode('utf8'), bcrypt.gensalt())
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user_id):
        user = SiteUser.query.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user

    @property
    def is_authenticated(self):
        return True

    def is_authenticated(self, data):
        users = SiteUser.query.all()
        auth_user = ''
        for user in users:
            if data['name'] == user.name:
                if bcrypt.checkpw(data['password'].encode('utf8'), user.password.encode('utf8')):
                    auth_user = user
                    print("passwords match")
                    return True
                else:
                    print("paswords dont match")
            else:
                return False
        return False

    def get_id(self):
        return self.id

    def is_active(self, data):
        if is_authenticaded(data):
            return True
        return False

    def is_anonymous(self):
        return False
