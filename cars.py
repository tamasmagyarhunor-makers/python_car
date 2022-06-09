from settings import *
import json

# Initialize our database
db = SQLAlchemy(app)

# the class Car will inherit the db.Model of SQLAlchemy
class Car(db.Model):
    __tablename__ = 'cars' # create cars table
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(20), nullable=False)
    model = db.Column(db.String(20), nullable=False)
    fuel_type = db.Column(db.String(20), nullable=False)
    gearbox = db.Column(db.String(20), nullable=False)
    year = db.Column(db.Date, nullable=False)
