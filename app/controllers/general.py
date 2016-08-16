from server import app

from flask import render_template
from flask import request
from flask import redirect
from flask import send_file

from models.code_snippet import CodeSnippet
from models.forms import ContactForm


@app.route('/')
def index():
    slug = '/'
    page_title = 'Home'
    return render_template('index.html', slug = slug, page_title = page_title)

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
