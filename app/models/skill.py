from server import db
from server import app


class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    category = db.Column(db.String(64))
    proficiency = db.Column(db.String(3))

    def get_all(self):
        skills = Skill.query.all()
        return skills

    def get_by_id(self, skill_id):
        skill = Skill.query.get(skill_id)
        return skill

    def create(self, data):
        skill = Skill()
        skill.title = data['title']
        skill.category = data['category']
        skill.proficiency = data['proficiency']
        db.session.add(skill)
        db.session.commit()
        return skill

    def update(self, data):
        skill = Skill.query.get(data['id'])
        skill.title = data['title']
        skill.category = data['category']
        skill.proficiency = data['proficiency']
        db.session.add(skill)
        db.session.commit()
        return skill

    def delete(self, skill_id):
        skill = Skill.query.get(skill_id)
        db.session.delete(skill)
        db.session.commit()
        return skill
