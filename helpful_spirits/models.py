from . import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    volunteers = db.relationship('Volunteer', backref='city')
    locations = db.relationship('Location', backref='city')

    @staticmethod
    def get_by_name(name):
        return City.query.filter_by(name=name).first()


class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50), nullable=False)
    number = db.Column(db.String(50), nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    posters = db.relationship('Poster', backref='location')

    @staticmethod
    def add_new_location(street, number, city_id):
        location = Location(street=street, number=number, city_id=city_id)
        db.session.add(location)
        db.session.commit()
        return Location.query.filter_by(street=street, number=number, city_id=city_id).first()


class User(db.Model, UserMixin):
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


class Victim(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    posters = db.relationship('Poster', backref='victim')


class Volunteer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)


class Specialisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    danger_level = db.Column(db.Integer, nullable=False)
    posters = db.relationship('Poster', backref='category')

    @staticmethod
    def get_by_name(name):
        return Category.query.filter_by(name=name).first()


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
