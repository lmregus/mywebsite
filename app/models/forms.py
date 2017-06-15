from flask_wtf import FlaskForm
from flask_wtf import RecaptchaField

from wtforms import Form
from wtforms import StringField
from wtforms import PasswordField
from wtforms import validators


class LoginForm(FlaskForm):
    username = StringField('Username', [
        validators.DataRequired(),
        validators.Length(min=4, max=20)
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
    ])
    recaptcha = RecaptchaField()
