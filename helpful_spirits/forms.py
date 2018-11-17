from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField, validators
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, urllib, EqualTo, Email

class SimpleForm(Form):
    name = StringField('description')


class Register(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repetition = PasswordField('Password repetition', validators=[DataRequired(), EqualTo(password, 'Passwords must match!')])
    birth_date = StringField('Date')
    mail = Email('Email')
    tel = StringField('Tel')


class Login(Form):
    username = StringField('Username')
    password = PasswordField('Password')


class SearchCity(Form):
    city_name = StringField('City')


class AddPoster(Form):
    start_date = StringField('Start date')
    end_date = StringField('End date')
    title = StringField('Title')
    description = StringField('Description')
    location = StringField('Location')
    category = StringField('Category')


