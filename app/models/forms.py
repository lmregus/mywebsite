from wtforms import Form
from wtforms import StringField
from wtforms import validators


class ContactForm(Form):
    name = StringField('Name', [validators.Length(min=10, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=40)])
    message = StringField('Message', [validators.Length(min=255, max=400)])
