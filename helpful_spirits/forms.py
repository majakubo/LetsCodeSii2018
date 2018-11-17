from flask_wtf import Form
from wtforms.fields import StringField
from flask_wtf.html5 import URLField
from wtforms.validators import DataRequired, urllib

class SimpleForm(Form):
    name = StringField('description')