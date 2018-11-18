import datetime

from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, DateField, SelectField
from wtforms.validators import DataRequired, EqualTo, Email

from .models import City, Category, Specialisation


class SimpleForm(Form):
    name = StringField('description')


class Register(Form):
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_repetition = PasswordField('Confirm password',
                                        validators=[DataRequired()])
    birth_date = DateField('Date', validators=[DataRequired()])
    mail = StringField('Email', validators=[DataRequired(), Email()])
    tel = StringField('Phone number', validators=[DataRequired()])


class Login(Form):
    mail = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class SearchCity(Form):
    city_name = StringField('City', validators=[DataRequired()])


class AddPoster(Form):
    city_choices = [(city.name, city.name) for city in City.get_all()]
    category_choices = [(category.name, category.name) for category in Category.get_all()]
    start_date = DateField('Start date', validators=[DataRequired()], default=datetime.datetime.now().date())
    end_date = DateField('End date', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    city = SelectField('City', choices=city_choices, validators=[DataRequired()])
    location_street = StringField('Street', validators=[DataRequired()])
    location_street_number = StringField('Street number', validators=[DataRequired()])
    category_name = SelectField('Category', choices=category_choices, validators=[DataRequired()])


class FilterSearch(Form):
    city_choices = [(city.name, city.name) for city in City.get_all()]
    category_choices = [(category.name, category.name) for category in Category.get_all()]
    specialisation_choices = [(specialisation.name, specialisation.name) for specialisation in Specialisation.get_all()]

    city = SelectField('City', choices=city_choices, validators=[DataRequired()])
    specialisation = SelectField('Specialization', choices=specialisation_choices)
    category_name = SelectField('Category', choices=category_choices, validators=[DataRequired()])


class VolunteersDeclaration(Form):
    city_choices = [(city.name, city.name) for city in City.get_all()]
    does_want = StringField('Declaration of choice', validators=[DataRequired()])
    does_accept = StringField('Please accept regulations', validators=[DataRequired()])
    specialisation_choices = [(specialisation.name, specialisation.name) for specialisation in Specialisation.get_all()]
    specialisation = SelectField('Choose specialisation', choices=specialisation_choices)
    city = SelectField('City', choices=city_choices, validators=[DataRequired()])
