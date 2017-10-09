from server import app

from flask import abort
from flask import render_template
from flask import request

from flask_login import login_required

from models.blog import Post


create_page_title = 'Create Post'
edit_page_title = 'Edit Post'
posts_per_page = 5

@app.route('/admin/blog/post')
@login_required
def blog():
    blog = Post()
    return render_template('/admin/post.html', posts = blog.get_all(), page_title = create_page_title)

@app.route('/admin/blog/post/create', methods = ['POST'])
@login_required
def create_post():
    blog = Post()
    posts = blog.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'description': request.form['description'],
            'content': request.form['content'],
            'status': int(request.form['status']),
        }
        post = blog.create(data)
        message = post.title + ' was created'
    else:
        message = 'There was an error trying to create post'
    return render_template('admin/post.html', posts = posts, message = message, page_title = create_page_title)

@app.route('/admin/blog/post/edit/<post_id>', methods = ['POST', 'GET'])
@login_required
def edit_post(post_id):
    post = Post().get_by_id(post_id)
    return render_template('admin/update_post.html', post = post, page_title = edit_page_title)

@app.route('/admin/blog/post/update', methods = ['POST'])
@login_required
def update_post():
    blog = Post()
    posts = blog.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'description': request.form['description'],
            'content': request.form['content'],
            'status': int(request.form['status']),
        }
        blog.update(data)
        message = data['title'] + ' was updated'
    else:
        message = 'There was an error trying to create post'
    return render_template('admin/post.html', posts = posts, message = message, page_title = edit_page_title)

@app.route('/admin/blog/post/delete/<int:post_id>')
@login_required
def delete_post(post_id):
    blog = Post()
    posts = blog.get_all()
    post = blog.delete(post_id)
    message = post.title + ' deleted'
    return render_template('admin/post.html', posts = posts, message = message, page_title = create_page_title)

@app.route('/blog/post/<slug>', methods = ['GET'])
def post(slug):
    blog = Post()
    posts = blog.get_all()
    post = blog.get_by_slug(slug)
    slugs = [p.slug for p in posts]
    if(slug not in slugs):
        abort(404)
    return render_template('pages/post.html', post = post)

@app.route('/blog/', methods = ['GET'])
@app.route('/blog/<int:page>', methods=['GET'])
def blog_home(page=1):
    blog = Post()
    posts = blog.get_publish().paginate(page, posts_per_page, False)
    return render_template('pages/blog.html', posts = posts)
