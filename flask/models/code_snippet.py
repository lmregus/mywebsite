from server import db
from server import app

class CodeSnippet(db.Model):
    __tablename__ = "code_snippet"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    code = db.Column(db.Text())

    def get_all(self):
        code_snippets = CodeSnippet.query.all()
        return code_snippets

    def get_by_id(self, snippet_id):
        code_snippet = CodeSnippet.query.get(snippet_id)
        return code_snippet

    def create(self, data):
        code_snippet = CodeSnippet(title = data['title'], code = data['code'])
        db.session.add(code_snippet)
        db.session.commit()
        return code_snippet

    def update(self, data):
        code_snippet = CodeSnippet.query.get(data['id'])
        code_snippet.title = data['title']
        code_snippet.code = data['code']
        db.session.add(code_snippet)
        db.session.commit()
        return code_snippet

    def delete(self, snippet_id):
        code_snippet = CodeSnippet.query.get(snippet_id)
        db.session.delete(code_snippet)
        db.session.commit()
        return code_snippet
