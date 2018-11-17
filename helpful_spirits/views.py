from helpful_spirits import app, db
from flask import render_template, redirect
from .models import *
from .forms import SimpleForm, Register, Login



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods= ('GET','POST'))
def login():
    form = Login()
    if form.validate_on_submit():
        #TODO: tutaj jakies odczytanko z bazy
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/simple_query', methods=('GET', 'POST'))
def query():
    form = SimpleForm()
    if form.validate_on_submit():
        return redirect('/posters')
    return render_template('simple_form_test.html', form=form)


@app.route('/register', methods=('GET','POST'))
def register():
    form = Register()
    if form.validate_on_submit():
        #TODO: tutaj jakies wpisanko do bazy
        return redirect('/')
    return render_template('register.html', form=form)


@app.route('/add_poster', methods=("GET", "POST"))
def add_poster():
    form = AddPoster()
    #todo
    if form.validate_on_submit():
        print("HERE")
        location_street = form.location_street.data
        location_street_number = form.location_street_number.data
        city = City(name=form.city.data)
        location = Location(street=location_street, number=location_street_number, city_id=city)
        category = Category(name=form.category_name.data)
        poster = Poster(title=form.title.data, description=form.description.data, start_date=form.start_date.data,
                        end_date=form.end_date.data, location=location, category=category)

        print("HERE")
        db.session.add(city)
        db.session.add(location)
        db.session.add(poster)
        db.session.commit()
    return render_template('add_poster.html', form=form)


@app.route('/posters')
def posters():
    posters = Poster.query.all()
    iterator_ = zip(posters, range(len(posters)))
    return render_template('posters.html', posters=iterator_)


@app.route('/posters/<id>')
def poster(id):
    return "you are at specific site"


@app.route('/my_profile')
def my_profile():
    return "You are in my profile site"


##########################################
# TODO
##########################################

@app.route('/add_cities')
def add_cities():
    db.session.add(City(name="Gdansk"))
    db.session.add(City(name="Gdynia"))
    db.session.add(City(name="Sopot"))
    db.session.add(City(name="Warszawa"))
    db.session.add(City(name="Krakow"))
    db.session.add(City(name="Katowice"))
    db.session.add(City(name="Grudziadz"))
    db.session.commit()
