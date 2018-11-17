from helpful_spirits import app

from .models import *


@app.route('/')
def index():
	city = City(name='Gdańsk')
	region = Region(name="Wrzeszcz", city_id=city)
	location = Location()
	#user = User()
	return region.city_id.name
