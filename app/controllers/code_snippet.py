from server import app

from flask import render_template
from flask import request
from flask import redirect
from flask_login import login_required

from models.code_snippet import CodeSnippet


create_page_title = 'Create Code Snippet'
edit_page_title = 'Edit Snippet'

@app.route('/admin/code-snippet')
@login_required
def snippet():
    code_snippets = CodeSnippet()
    return render_template('/admin/code_snippet.html', code_snippets = code_snippets.get_all(), page_title = create_page_title)

@app.route('/admin/code-snippet/create', methods = ['POST'])
@login_required
def create_snippet():
    code_snippet = CodeSnippet()
    code_snippets = code_snippet.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'github_url': request.form['github_url'],
            'programming_language': request.form['programming_language'],
            'code': request.form['code'],
        }
        code_snippet = code_snippet.create(data)
        message = code_snippet.title + ' was created'
    else:
        message = 'There was an error trying to create the entry'

    return render_template('admin/code_snippet.html', code_snippets = code_snippets, message = message)

@app.route('/admin/code-snippet/edit/<snippet_id>', methods = ['POST', 'GET'])
@login_required
def edit_snippet(snippet_id):
    code_snippet = CodeSnippet().get_by_id(snippet_id)
    return render_template('admin/update_code_snippet.html', code_snippet = code_snippet, page_title = edit_page_title)

@app.route('/admin/code-snippet/update', methods = ['POST'])
@login_required
def update_snippet():
    code_snippet = CodeSnippet()
    code_snippets = code_snippet.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'github_url': request.form['github_url'],
            'programming_language': request.form['programming_language'],
            'code': request.form['code'],
        }
        code_snippet = code_snippet.update(data)
        message = code_snippet.title + ' was updated'
    else:
        message = 'There was an error trying to update the entry'
    return render_template('admin/code_snippet.html', code_snippets = code_snippets, message = message, page_title = create_page_title)

@app.route('/admin/code-snippet/delete/<snippet_id>')
@login_required
def delete_snippet(snippet_id):
    code_snippet = CodeSnippet()
    code_snippets = code_snippet.get_all()
    code_snippet = code_snippet.delete(snippet_id)
    message = code_snippet.title + ' deleted'
    return render_template('admin/code_snippet.html', code_snippets = code_snippets, message = message, page_title = create_page_title)
