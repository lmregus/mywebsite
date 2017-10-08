from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField

from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import validators
from wtforms import TextAreaField
from wtforms import SelectField


class LoginForm(FlaskForm):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    recaptcha = RecaptchaField()

class CreatePost(FlaskForm):
    title = StringField('Title', [
        validators.DataRequired(),
        validators.Length(min=20, max=128)
    ])
    description = StringField('Description')
    content = TextAreaField('Content', [
        validators.DataRequired()
    ])
    status = SelectField('Status', choices=[(0, 'Draft'), (1, 'Published')])
