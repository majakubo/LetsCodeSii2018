import datetime

from flask import render_template, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from helpful_spirits import app, db

from .forms import Register, Login, AddPoster, FilterSearch
from .models import *


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
    db.session.add(Category(name='any', danger_level=10))
    db.session.add(Specialisation(name="Doctor"))
    db.session.add(Specialisation(name="Electrician"))
    db.session.add(Specialisation(name="Firefighter"))
    db.session.add(Specialisation(name="Nurse"))
    db.session.add(Specialisation(name="Driver"))
    db.session.add(Specialisation(name="Painter"))
    db.session.add(Specialisation(name="Anything"))
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
        user = User.get_by_mail(form.mail.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('posters'))
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/register', methods=('GET', 'POST'))
def register():
    form = Register()
    if form.validate_on_submit():
        if User.get_by_mail(form.mail.data) is not None:
            return render_template('register.html', form=form)

        if form.password.data != form.password_repetition.data:
            return render_template('register.html', form=form)
        password = generate_password_hash(form.password.data)
        user = User(firstname=form.name.data,
                    surname=form.surname.data,
                    birthday=form.birth_date.data,
                    phone=form.tel.data,
                    password_hash=password,
                    email=form.mail.data)

        db.session.add(user)
        db.session.commit()

        return redirect('/')
    return render_template('register.html', form=form)


@app.route('/add_poster', methods=("GET", "POST"))
@login_required
def add_poster():
    form = AddPoster()
    form.cities = City.get_all()
    if current_user is not None and form.validate_on_submit():
        city = City.get_by_name(form.city.data)
        category = Category.get_by_name(form.category_name.data)

        if city is None:
            form.city_error = True
            return render_template('add_poster.html', form=form)
        if category is None:
            form.category_error = True
            return render_template('add_poster.html', form=form)
        if form.end_date.data < form.start_date.data or form.end_date.data < date.today():
            form.date_error = True
            return render_template('add_poster.html', form=form)

        location = Location.add_new_location(form.location_street.data, form.location_street_number.data, city.id)

        db.session.add(Poster(add_date=datetime.datetime.now().date(),
                              title=form.title.data, description=form.description.data, start_date=form.start_date.data,
                              is_active=True, end_date=form.end_date.data, location_id=location.id, category=category,
                              victim_id=current_user.id))
        db.session.commit()
        poster_id = Poster.query.filter_by(title=form.title.data).filter_by(add_date=datetime.datetime.now().date()) \
            .filter_by(description=form.description.data).filter_by(start_date=form.start_date.data).first().id

        send_to_close_volunteers(city.id, poster_id)
        return redirect(url_for('posters'))

    return render_template('add_poster.html', form=form)


@app.route('/posters', methods=['GET', 'POST'])
def posters():
    form = FilterSearch()
    if form.validate_on_submit():
        specific_posters = Poster.get_specific(category=form.category_name.data, city=form.city.data,
                                               specialization=None)
        iterator_ = zip(specific_posters, range(len(specific_posters)))
        return render_template('posters.html', posters=iterator_, form=form)
    else:
        all_active_posters = Poster.get_all_active()
        iterator_ = zip(all_active_posters, range(len(all_active_posters)))
        return render_template('posters.html', posters=iterator_, form=form)


@app.route('/posters/<id>')
def poster(id):
    form = AddPoster()
    poster = Poster.get_by_id(id)
    if poster is None:
        return redirect(url_for('posters'))
    victim = Victim.find_user_by_id(poster.victim_id)
    return render_template('poster.html', poster=poster, form=form, victim=victim)


@app.route('/my_profile')
@login_required
def my_profile():
    return render_template('my_profile.html')


# todo
@app.route('/volunteers')
def volunteers():
    volunteers = Volunteer.get_all()
    users_id = [volunteer.id for volunteer in Volunteer.get_all()]
    users = [User.query.filter_by(id=user_id) for user_id in users_id]
    users = set(users) - {None}
    iterator_ = zip(volunteers, range(len(volunteers)))
    user_iterator_ = zip(users, range(len(users)))
    return render_template('volunteers.html', volunteers=iterator_, users=user_iterator_)


# todo
@app.route('/volunteers/<id>')
def concrete_volunteer(id):
    volunteer = Volunteer.get_volunteer(id)
    if volunteer is None:
        return redirect(url_for('volunteers'))
    return render_template('volunteer.html', volunteer=volunteer)


# todo
@staticmethod
def send_to_close_volunteers(city_id, poster_id):
    close_volunteers = Volunteer.query.filter_by(city_id=city_id).all()
    for volunteer in close_volunteers:
        invited.insert(volunteer_id=volunteer.id, poster_id=poster_id, status='INVITED')
