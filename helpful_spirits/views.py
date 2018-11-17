from helpful_spirits import app
from flask import render_template
from .models import *
from .forms import SimpleForm

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/my')
def my():
	city = City(name='Gdansk')
	region = Region(name="Wrzeszcz", city_id=city)
	
	location = Location()
	#user = User()
	#poster = Poster()
	return region.city_id.name

@app.route('/login')
def login():
    return "You are in login site"


@app.route('/simple_query')
def login():
    form = SimpleForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)


@app.route('/register')
def register():
    return "You are in register site"


@app.route('/add_poster')
def add_poster():
    return "You are in add poster site"


@app.route('/posters')
def posters():
    return "You are in posters site"


@app.route('/posters/<id>')
def poster(id):
    return "you are at specific site"


@app.route('/my_profile')
def my_profile():
    return "You are in my profile site"
