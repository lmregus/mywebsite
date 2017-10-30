from server import db
from server import app

from datetime import datetime


'''
    This is only a simple CRUD for blog posts,
    more features, like adding comments(maybe discourse integration)
    or related blogs will be added in the future
'''
class Post(db.Model):
    __tablename__="post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    description = db.Column(db.String(512))
    content = db.Column(db.String(50000))
    slug = db.Column(db.String(128))
    status = db.Column(db.Integer)      #0 draft, 1 published
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.now)
    upd_date = db.Column(db.DateTime, onupdate=datetime.now)

    def get_all(self):
        posts = Post.query.order_by(Post.pub_date.desc())
        return posts

    def get_publish(self):
        posts = Post.query.filter(Post.status == 1)
        return posts

    def get_by_id(self, post_id):
        post = Post.query.get(post_id)
        return post

    def get_by_slug(self, slug):
        posts = Post.query.all()
        post = None
        for p in posts:
            if p.slug == slug:
                post = p
        return post

    def create(self, data):
        post = Post()
        post.title = data['title']
        post.description = data['description']
        post.content = data['content']
        post.slug = data['title'].lower().replace(' ', '-')
        post.status = data['status']
        db.session.add(post)
        db.session.commit()
        return post

    def update(self, data):
        post = Post.query.get(data['id'])
        post.title = data['title']
        post.description = data['description']
        post.content = data['content']
        post.slug = data['title'].lower().replace(' ', '-')
        post.status = data['status']
        db.session.add(post)
        db.session.commit()

    def delete(self, post_id):
        post = Post.query.get(post_id)
        db.session.delete(post)
        db.session.commit()
        return post

    def get_url(self):
        return "blog/" + self.slug
