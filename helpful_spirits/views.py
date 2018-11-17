import datetime

from helpful_spirits import app, db
from flask import render_template, redirect
from .models import *
from .forms import SimpleForm, Register, Login, AddPoster


# todo
@app.route('/')
def index():
    Category.query.delete()
    City.query.delete()
    db.session.add(City(name="Gdansk"))
    db.session.add(City(name="Gdynia"))
    db.session.add(City(name="Sopot"))
    db.session.add(City(name="Warszawa"))
    db.session.add(City(name="Krakow"))
    db.session.add(City(name="Katowice"))
    db.session.add(City(name="Grudziadz"))
    db.session.add(Category(name="Flood", danger_level=8))
    db.session.add(Category(name="Tsunami", danger_level=10))
    db.session.add(Category(name="Earthquake", danger_level=10))
    db.session.add(Category(name="Disease", danger_level=4))
    db.session.add(Category(name="Renovation", danger_level=2))
    db.session.add(Category(name="Volcano", danger_level=2))
    db.session.add(Category(name="Epidemic", danger_level=2))
    db.session.add(Category(name="No electricity", danger_level=8))
    db.session.add(Category(name="No internet", danger_level=10))
    db.session.add(Category(name="Charity", danger_level=2))
    db.session.commit()
    return render_template("index.html")


@app.route('/login', methods=('GET', 'POST'))
def login():
    form = Login()
    if form.validate_on_submit():
        # TODO: tutaj jakies odczytanko z bazy
        return redirect('/')
    return render_template('login.html', form=form)


@app.route('/simple_query', methods=('GET', 'POST'))
def query():
    form = SimpleForm()
    if form.validate_on_submit():
        return redirect('/posters')
    return render_template('simple_form_test.html', form=form)


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = Register()
    if form.validate_on_submit():
        # TODO: tutaj jakies wpisanko do bazy
        return redirect('/')
    return render_template('register.html', form=form)


@app.route('/add_poster', methods=("GET", "POST"))
def add_poster():
    form = AddPoster()
    # todo
    if form.validate_on_submit():
        city = City.get_by_name(form.city.data)
        category = Category.get_by_name(form.category_name.data)

        if city is None:
            form.city_error = True
            return render_template('add_poster.html', form=form)
        if category is None:
            form.category_error = True
            return render_template('add_poster.html', form=form)

        location = Location.add_new_location(form.location_street.data, form.location_street_number.data, city.id)

        # victim id TODO
        poster = Poster(add_date=datetime.datetime.now().date(),
                        title=form.title.data, description=form.description.data, start_date=form.start_date.data,
                        is_active=False, end_date=form.end_date.data, location_id=location.id, category=category,
                        victim_id=1)

        db.session.add(poster)
        db.session.commit()
        print("HERAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAaE")
    return render_template('add_poster.html', form=form)


@app.route('/posters')
def posters():
    return render_template('posters.html', posters=Poster.query.all())


@app.route('/posters/<id>')
def poster(id):
    return "you are at specific site"


@app.route('/my_profile')
def my_profile():
    return "You are in my profile site"
