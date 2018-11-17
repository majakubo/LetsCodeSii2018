from flask_wtf import Form
from wtforms.fields import StringField, BooleanField, PasswordField, DateField
from flask_wtf.html5 import URLField
import datetime
from wtforms.validators import DataRequired, EqualTo, Email


class SimpleForm(Form):
    name = StringField('description')


class Register(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repetition = PasswordField('Password repetition', validators=[DataRequired(), EqualTo(password, 'Passwords must match!')])
    birth_date = StringField('Date', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    tel = StringField('Tel', validators=[DataRequired()])


class Login(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class SearchCity(Form):
    city_name = StringField('City', validators=[DataRequired()])


class AddPoster(Form):
    start_date = DateField('Start date', validators=[DataRequired()], default=datetime.datetime.now().date())
    end_date = DateField('End date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
