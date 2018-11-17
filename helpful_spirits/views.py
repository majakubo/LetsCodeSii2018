from helpful_spirits import app, db
from flask import render_template
from .models import *
from .forms import SimpleForm


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return "You are in login site"


@app.route('/simple_query')
def query():
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
    return render_template('posters.html', posters=Poster.query.all())


@app.route('/posters/<id>')
def poster(id):
    return "you are at specific site"


@app.route('/my_profile')
def my_profile():
    return "You are in my profile site"


# TODO
@app.route('/testdata')
def test_data():
    Poster.query.delete()
    p1 = Poster(is_active=True, title='ELO')
    p2 = Poster(is_active=False, title='ELO')
    p3 = Poster(is_active=False, title='bykankub')
    p4 = Poster(is_active=False, title='Siemanko byku')
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.commit()
    
