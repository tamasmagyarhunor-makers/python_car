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

    def json(self):
        return {
            'id': self.id,
            'make': self.make,
            'model': self.model,
            'fuel_type': self.fuel_type,
            'gearbox': self.gearbox,
            'year': self.year
        } # this method will convert our output to json

    def add_car(_make, _model, _fuel_type, _gearbox, _year):
        '''CREATE new Car'''
        # create an instance of Car constructor
        new_car = Car(
            make = _make,
            model = _model,
            fuel_type = _fuel_type, 
            gearbox = _gearbox,
            year = _year
        )

        db.session.add(new_car) # add movie to db session
        db.session.commit() # commit changes to session

    def get_all_cars():
        '''GET all Cars'''
        return [Car.json(car) for car in Car.query.all()]

    def get_car(_id):
        '''GET a Car by id'''
        return [Car.json(Car.query.filter_by(id = _id).first())]

    def update_car(_id, _make, _model, _fuel_type, _gearbox, _year):
        '''UPDATE a car by id'''
        car_to_update = Car.query.filter_by(id = _id).first()
        car_to_update.make = _make
        car_to_update.model = _model
        car_to_update.fuel_type = _fuel_type
        car_to_update.gearbox = _gearbox
        car_to_update.year = _year
        db.session.commit()

    def delete_car(_id):
        '''DELETE a car by id'''
        Car.query.filter_by(id = _id).delete()
        db.session.commit()
