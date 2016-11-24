from server import app

from flask import render_template
from flask import request
from flask import redirect

from models.skill import Skill

create_page_title = 'Create Skill'
edit_page_title = 'Edit Skill'


@app.route('/admin/skill')
def skill():
    skills = Skill()
    return render_template('/admin/skill.html', skills = skills.get_all(),
                            page_title = create_page_title)

@app.route('/admin/skill/create', methods = ['POST'])
def create_skill():
    skill = Skill()
    skills = Skill().get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'title': request.form['title'],
            'proficiency': request.form['proficiency'],
            'category': request.form['category'],
        }
        skill = skill.create(data)
        message = skill.title + ' was created'
    else:
        message = 'There was an error trying to create the entry'

    return render_template('/admin/skill.html', skills = skills, message = message)
'''
@app.route('/code-snippet/edit/<snippet_id>', methods = ['POST', 'GET'])
def edit_snippet(snippet_id):
    code_snippet = CodeSnippet().get_by_id(snippet_id)
    return render_template('admin/update_code_snippet.html', code_snippet = code_snippet, page_title = edit_page_title)

@app.route('/code-snippet/update', methods = ['POST'])
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

@app.route('/code-snippet/delete/<snippet_id>')
def delete_snippet(snippet_id):
    code_snippet = CodeSnippet()
    code_snippets = code_snippet.get_all()
    code_snippet = code_snippet.delete(snippet_id)
    message = code_snippet.title + ' deleted'
    return render_template('admin/code_snippet.html', code_snippets = code_snippets, message = message, page_title = create_page_title)
    '''
