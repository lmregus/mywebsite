from server import app
from server import login_manager

from flask import render_template
from flask import request
from flask import redirect
from flask import send_file
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from models.code_snippet import CodeSnippet
from models.forms import ContactForm
from models.skill import Skill
from models.job import Job
from models.education import Degree
from models.site_user import SiteUser


@login_manager.user_loader
def load_user(user_id):
    return SiteUser().get_by_id(user_id)

@app.route('/')
def index():
    slug = '/'
    form = ContactForm(request.form)
    skill = Skill()
    job = Job()
    jobs = job.get_all()
    jobs.sort(key=lambda date:date.start_date, reverse=True)
    education = Degree()
    page_title = 'Home'
    return render_template('index.html', slug = slug, 
                            page_title = page_title, 
                            form = form, skills = skill.get_all(),
                            jobs = jobs,
                            education = education.get_all())

@app.route('/resume')
def resume_page():
    page_title = 'Resume'
    slug = 'resume'
    try:
        return send_file('static/pdfs/LuisRegusCV3.pdf', attachment_filename='LuisRegusCV3.pdf')
    except Exception as e:
        return str(e)
    #return render_template('pages/resume.html', slug = slug, page_title = page_title)

@app.route('/code-snippets')
def code_snippets():
    page_title = 'Code Snippets'
    code_snippets = CodeSnippet().get_all()
    slug = 'code-snippets'
    return render_template('pages/code-snippets.html', slug = slug, page_title = page_title, code_snippets = code_snippets)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    page_title = 'Contact Me'
    slug = 'contact'
    #code to send form using email
    #if request.method == 'POST' and form.validate(): 
    return render_template('pages/contact.html', slug = slug, page_title = page_title, form = form)

@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = {
            'name': request.form['username'],
            'password': request.form['password']
        }
        user = SiteUser().get_by_username(data['name'])
        if user.is_authenticated(data):
            login_user(user)
            return redirect('/admin/code-snippet')
    return render_template('admin/login.html')

@app.route('/admin/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/') 
