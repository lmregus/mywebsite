from server import db
from server import app

class CodeSnippet(db.Model):
    __tablename__ = "code_snippet"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    code = db.Column(db.Text())
    github_url = db.Column(db.String(256))
    programming_language = db.Column(db.String(128))

    def get_all(self):
        code_snippets = CodeSnippet.query.all()
        return code_snippets

    def get_by_id(self, snippet_id):
        code_snippet = CodeSnippet.query.get(snippet_id)
        return code_snippet

    def create(self, data):
        code_snippet = CodeSnippet()
        code_snippet.title = data['title']
        code_snippet.code = data['code']
        code_snippet.github_url = data['github_url']
        code_snippet.programming_language = data['programming_language']
        db.session.add(code_snippet)
        db.session.commit()
        return code_snippet

    def update(self, data):
        code_snippet = CodeSnippet.query.get(data['id'])
        code_snippet.title = data['title']
        code_snippet.code = data['code']
        code_snippet.github_url = data['github_url']
        code_snippet.programming_language = data['programming_language']
        db.session.add(code_snippet)
        db.session.commit()
        return code_snippet

    def delete(self, snippet_id):
        code_snippet = CodeSnippet.query.get(snippet_id)
        db.session.delete(code_snippet)
        db.session.commit()
        return code_snippet
