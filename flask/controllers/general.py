from server import app

from flask import render_template
from flask import request
from flask import redirect


@app.route('/')
def index():
    slug = '/'
    return render_template('index.html', slug = slug)

@app.route('/resume')
def resume_page():
    page_title = 'Resume'
    slug = 'resume'
    return render_template('pages/resume.html', slug = slug, page_title = page_title)

@app.route('/code-snippets')
def code_snippets():
    page_title = 'Code Snippets'
    slug = 'code-snippets'
    return render_template('pages/code-snippets.html', slug = slug, page_title = page_title)

@app.route('/contact')
def contact():
    page_title = 'Contact Me'
    slug = 'contact'
    return render_template('pages/contact.html', slug = slug, page_title = page_title)
