from helpful_spirits import app
from flask import render_template, redirect
from .models import *
from .forms import SimpleForm


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return "You are in login site"


<<<<<<< HEAD
@app.route('/simple_query', methods=('GET','POST'))
def simple():
=======
@app.route('/simple_query')
def query():
>>>>>>> b92c038e5e29c1a653f3e0c823834f74815458dd
    form = SimpleForm()
   # if form.validate_on_submit():
    return redirect('/test')
    return render_template("simple_form_test.html", form=form)

@app.route('/test')
def testtt():
    return render_template('test.html')


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


<<<<<<< HEAD

=======
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
    
>>>>>>> b92c038e5e29c1a653f3e0c823834f74815458dd
