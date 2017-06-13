from server import app

from flask import render_template
from flask import request
from flask import redirect
from flask_login import login_required

from models.skill import Skill

create_page_title = 'Create Skill'
edit_page_title = 'Edit Skill'


@app.route('/admin/skill')
@login_required
def skill():
    skills = Skill()
    return render_template('/admin/skill.html', skills = skills.get_all(),
                            page_title = create_page_title)

@app.route('/admin/skill/create', methods = ['POST'])
@login_required
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

@app.route('/admin/skill/edit/<skill_id>', methods = ['POST', 'GET'])
@login_required
def edit_skill(skill_id):
    skill = Skill().get_by_id(skill_id)
    return render_template('admin/update_skill.html', skill = skill, 
                            page_title = edit_page_title)

@app.route('/admin/skill/update', methods = ['POST'])
@login_required
def update_skill():
    skill = Skill()
    skills = skill.get_all()
    message = ''
    if request.method == 'POST':
        data = {
            'id': request.form['id'],
            'title': request.form['title'],
            'proficiency': request.form['proficiency'],
            'category': request.form['category'],
        }
        skill = skill.update(data)
        message = skill.title + ' was updated'
    else:
        message = 'There was an error trying to update the entry'
    return render_template('admin/skill.html', skills = skills, 
                            message = message, 
                            page_title = create_page_title)

@app.route('/admin/skill/delete/<skill_id>')
@login_required
def delete_skill(skill_id):
    skill = Skill()
    skills = skill.get_all()
    skill = skill.delete(skill_id)
    message = skill.title + ' deleted'
    return render_template('admin/skill.html', skills = skills, 
                            message = message, 
                            page_title = create_page_title)
