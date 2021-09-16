from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/Cyber_Link_GBU_2022'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_RECYCLE'] = 30
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 40


db = SQLAlchemy(app)
db.create_all()

# Diagrama base de datos - Database diagram ::::::
# https://docs.google.com/drawings/d/1yPsAwcgLrZl_9ui5iSGcvJf1lK7UsoHk7CYx_2_HPjM/edit?usp=sharing

class Event(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    details = db.Column(db.Text, nullable=False)
    dateStart = db.Column(db.DateTime, nullable=False)
    dateFinish = db.Column(db.DateTime, nullable=False)
    capacity = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '%r' % self.name


class Presentation(db.Model):

    id = db.Column(db.String(9), primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    details = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    approved = db.Column(db.Boolean, nullable=True)
    vote_yes = db.Column(db.Integer, unique=False, nullable=True) 
    vote_no = db.Column(db.Integer, unique=False, nullable=True)
    vote_white = db.Column(db.Integer, unique=False, nullable=True)
    vote_null = db.Column(db.Integer, unique=False, nullable=True) 

    # Relationship ::::::
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'),
        nullable=False)
    event = db.relationship('Event',
        backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '%r' % self.name



class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class Nationality(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class LocalGroup(db.Model):
    __tablename__ = 'localGroup'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    details = db.Column(db.Text, nullable=False)


class User(db.Model):

    id = db.Column(db.String(11), primary_key=True, unique=True) # Rut
    names = db.Column(db.String(80), unique=False, nullable=False)
    lastname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    dateOfBirth = db.Column(db.DateTime, nullable=True)
    vegetarian = db.Column(db.Boolean, nullable=False)
    phone = db.Column(db.String(12), unique=False, nullable=False)
    emergencyNumber = db.Column(db.String(12), unique=False, nullable=False)

    # Relationship ::::::
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'),
        nullable=True)
    role = db.relationship('Role',
        backref=db.backref('posts', lazy=True))


    nationality_id = db.Column(db.Integer, db.ForeignKey('nationality.id'),
        nullable=True)
    nationality = db.relationship('Nationality',
        backref=db.backref('posts', lazy=True))


    localGroup_id = db.Column(db.Integer, db.ForeignKey('localGroup.id'),
        nullable=True)
    localGroup = db.relationship('LocalGroup',
        backref=db.backref('posts', lazy=True, remote_side='LocalGroup.id'))

    def __repr__(self):
        return '%r' % self.name