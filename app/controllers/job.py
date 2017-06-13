from server import app

from flask import render_template
from flask import request
from flask import redirect
from flask_login import login_required

from models.job import Job

create_page_title = 'Create Job'
edit_page_title = 'Edit Job'


@app.route('/admin/job')
@login_required
def job():
    jobs = Job()
    return render_template('/admin/job.html', jobs = jobs.get_all(),
                            page_title = create_page_title)

@app.route('/admin/job/create', methods = ['POST'])
@login_required
def create_job():
    job = Job()
    jobs = Job().get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'company': request.form['company'],
            'description': request.form['description'],
        }
        job = job.create(data)
        message = job.title + ' was created'
    else:
        message = 'There was an error trying to create the entry'

    return render_template('/admin/job.html', jobs = jobs, message = message)

@app.route('/admin/job/edit/<job_id>', methods = ['POST', 'GET'])
@login_required
def edit_job(job_id):
    job = Job().get_by_id(job_id)
    return render_template('admin/update_job.html', job = job, 
                            page_title = edit_page_title)

@app.route('/admin/job/update', methods = ['POST'])
@login_required
def update_job():
    job = Job()
    jobs = job.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'start_date': request.form['start_date'],
            'end_date': request.form['end_date'],
            'company': request.form['company'],
            'description': request.form['description'],
        }
        job = job.update(data)
        message = job.title + ' was updated'
    else:
        message = 'There was an error trying to update the entry'
    return render_template('admin/job.html', jobs = jobs, 
                            message = message, 
                            page_title = create_page_title)

@app.route('/admin/job/delete/<job_id>')
@login_required
def delete_job(job_id):
    job = Job()
    jobs = job.get_all()
    job = job.delete(job_id)
    message = job.title + ' deleted'
    return render_template('admin/job.html', jobs = jobs, 
                            message = message, 
                            page_title = create_page_title)
