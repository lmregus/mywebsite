from server import app
from server import login_manager

from flask import render_template
from flask import request
from flask import redirect
from flask import send_file
from flask import abort
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required

from models.code_snippet import CodeSnippet
from models.skill import Skill
from models.job import Job
from models.education import Degree
from models.site_user import SiteUser
from models.forms import LoginForm


@login_manager.user_loader
def load_user(user_id):
    return SiteUser().get_by_id(user_id)

@app.route('/')
def index():
    slug = '/'
    skill = Skill()
    job = Job()
    jobs = job.get_all()
    jobs.sort(key=lambda date:date.start_date, reverse=True)
    education = Degree()
    page_title = 'Home'
    return render_template('index.html', slug = slug, 
                            page_title = page_title, 
                            skills = skill.get_all(),
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

@app.route('/code-snippets')
def code_snippets():
    page_title = 'Code Snippets'
    code_snippets = CodeSnippet().get_all()
    slug = 'code-snippets'
    return render_template('pages/code-snippets.html', slug = slug, page_title = page_title, code_snippets = code_snippets)

@app.route('/admin/login', methods=['GET', 'POST'])
@app.route('/admin/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = {
            'name': form.username.data,
            'password': form.password.data
        }
        user = SiteUser().get_by_username(data['name'])
        if user.is_authenticated(data):
            login_user(user)
            return redirect('/admin/code-snippet')
    return render_template('admin/login.html', form=form)

@app.route('/admin/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect('/') 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
