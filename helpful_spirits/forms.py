import datetime

from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, DateField
from wtforms.validators import DataRequired, EqualTo, Email


class SimpleForm(Form):
    name = StringField('description')


class Register(Form):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repetition = PasswordField('Confirm password',
                                        validators=[DataRequired(), EqualTo(password, message='Passwords must match!')])
    birth_date = StringField('Date', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    tel = StringField('Phone number', validators=[DataRequired()])


class Login(Form):
    mail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class SearchCity(Form):
    city_name = StringField('City', validators=[DataRequired()])


class AddPoster(Form):
    start_date = DateField('Start date', validators=[DataRequired()], default=datetime.datetime.now().date())
    end_date = DateField('End date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    location_street = StringField('Street', validators=[DataRequired()])
    location_street_number = StringField('Street number', validators=[DataRequired()])
    category_name = StringField('Category', validators=[DataRequired()])
