from . import db
from werkzeug.security import check_password_hash, generate_password_hash


# todo potem chyba wszystkie nulalble trzeba wpisac false

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    regions = db.relationship('Region', backref='city')


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    volunteers = db.relationship('Volunteer', backref='region')
    locations = db.relationship('Location', backref='region')


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)
    posters = db.relationship('Poster', backref='location')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posters = db.relationship('Poster', backref='victim')


class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'), nullable=False)


class Specialisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    danger_level = db.Column(db.Integer, nullable=False)
    posters = db.relationship('Poster', backref='category')


class Poster(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    add_date = db.Column(db.Date, nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date)
    is_active = db.Column(db.Boolean, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'), nullable=False)
    victim_id = db.Column(db.Integer, db.ForeignKey('victim.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)


invited = db.Table('invited',
                   db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id')),
                   db.Column('poster_id', db.Integer, db.ForeignKey('poster.id')))

vol_spec = db.Table('vol_spec',
                    db.Column('volunteer_id', db.Integer, db.ForeignKey('volunteer.id')),
                    db.Column('specialisation_id', db.Integer, db.ForeignKey('specialisation.id')))

spec_cat = db.Table('spec_cat',
                    db.Column('specialisation_id', db.Integer, db.ForeignKey('specialisation.id')),
                    db.Column('category_id', db.Integer, db.ForeignKey('category.id')))
