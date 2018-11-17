from helpful_spirits import app
from flask import render_template
from .models import *


@app.route('/my')
def my():
	city = City(name='Gdańsk')
	region = Region(name="Wrzeszcz", city_id=city)
	location = Location()
	#user = User()
	return region.city_id.name


@app.route('/')
def index():
	return render_template("index.html")

