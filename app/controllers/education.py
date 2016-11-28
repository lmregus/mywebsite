from server import app

from flask import render_template
from flask import request
from flask import redirect

from models.education import Degree


create_page_title = 'Create Degree'
edit_page_title = 'Edit Degree'

@app.route('/admin/education')
def degree():
    degrees = Degree()
    return render_template('/admin/degree.html', degrees = degrees.get_all(), page_title = create_page_title)

@app.route('/admin/education/create', methods = ['POST'])
def create_degree():
    degree = Degree()
    degrees = degree.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'school': request.form['school'],
            'type': request.form['type'],
            'description': request.form['description'],
            'date': request.form['date'],
        }
        degree = degree.create(data)
        message = degree.title + ' was created'
    else:
        message = 'There was an error trying to create the entry'

    return render_template('admin/degree.html', degrees = degrees, message = message)

@app.route('/admin/education/edit/<degree_id>', methods = ['POST', 'GET'])
def edit_degree(degree_id):
    degree = Degree().get_by_id(degree_id)
    return render_template('admin/update_degree.html', degree = degree, page_title = edit_page_title)

@app.route('/admin/education/update', methods = ['POST'])
def update_degree():
    degree = Degree()
    degrees = degree.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'school': request.form['school'],
            'type': request.form['type'],
            'description': request.form['description'],
            'date': request.form['date']
        }
        degree = degree.update(data)
        message = degree.title + ' was updated'
    else:
        message = 'There was an error trying to update the entry'
    return render_template('admin/degree.html', degrees = degrees, message = message, page_title = create_page_title)

@app.route('/admin/education/delete/<degree_id>')
def delete_degree(degree_id):
    degree = Degree()
    degrees = degree.get_all()
    degree = degree.delete(degree_id)
    message = degree.title + ' deleted'
    return render_template('admin/degree.html', degrees = degrees, message = message, page_title = create_page_title)
