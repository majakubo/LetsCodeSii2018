from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField

class SimpleForm(Form):
    name = StringField('description')
