from . import db
from werkzeug.security import check_password_hash, generate_password_hash


# todo potem chyba wszystkie nulalble trzeba wpisac false
# todo potem dodac relationshipy w druga strone

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    regions = db.relationship('Region', backref='region')


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    # volunteers = db.relationship('Volunteer', backref='volunteer')
    locations = db.relationship('Location', backref='location')


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50))
    number = db.Column(db.String(50))
    region = db.Column(db.Integer, db.ForeignKey('region.id'))
#    posters = db.relationship('Poster', backref='poster')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    phone = db.Column(db.String)
    password_hash = db.Column(db.String)
    #victim_id = db.relationship('Victim.id',uselist=False, backref='user')

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


#class Victim(User):
 #   id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

"""
class Volunteer(User):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    is_active = db.Column(db.Boolean, default=False)
    region = db.Column(db.Integer, db.ForeignKey('region.id'))


class Specialisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    danger_level = db.Column(db.Integer)


class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_date = db.Column(db.Date)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean)
    title = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    victim = db.Column(db.Integer, db.ForeignKey('victim.id'))
    location = db.Column(db.Integer, db.ForeignKey('location.id'))
    category = db.Column(db.Integer, db.ForeignKey('category.id'))


invited = db.Table('invited',
                   db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id')),
                   db.Column('poster_id', db.Integer, db.ForeignKey('poster.id')))

vol_spec = db.Table('vol_spec',
                    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id')),
                    db.Column('specialisation_id', db.Integer, db.ForeignKey('specialisation.id')))

spec_cat = db.Table('spec_cat',
                    db.Column('specialisation_id', db.Integer, db.ForeignKey('specialisation.id')),
                    db.Column('category_id', db.Integer, db.ForeignKey('category.id')))
"""
