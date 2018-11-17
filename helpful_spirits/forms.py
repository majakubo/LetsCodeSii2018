from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField, validators
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, urllib

class SimpleForm(Form):
    name = StringField('description')


class Register(Form):
    username = StringField('Username')
    password
    password_repetition
    birth_date
    mail
    tel


class Login(Form):
    username
    password


class SearchCity(Form):
    city_name


class AddPoster(Form):
    start_date
    end_date
    title
    description
    location
    category


