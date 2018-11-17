from helpful_spirits import app, db
from flask import render_template, redirect, flash, request, url_for
from .models import *
from flask_login import login_required, login_user

from .forms import SimpleForm, Register, Login


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/foo', methods=["GET", "POST"])
@login_required
def foo():
    return "only logged in user can reach this site"

@app.route('/login', methods= ('GET','POST'))
def login():
    form = Login()
    if form.validate_on_submit():
        #TODO: tutaj jakies odczytanko z bazy
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user)
            flash('Logged in successfully as {}.'.format(user.firstname))
            return redirect(request.args.get('next') or url_for('index'))
        flash('Incorrect username or password.')
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
    return render_template('posters.html', posters=Poster.query.all())


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
