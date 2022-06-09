# Python CRUD app with Flask, Flask_SQLAlchemy

This is an extremely small API using Python3, Flask, Flask_SQLAlchemy(ORM) and a SQLite database.

In your terminal, run the following code to install dependencies:
```
>>> pip install flask
>>> pip install flask-sqlalchemy
```

In your terminal, run the following code to create the database and cars table and its columns
```
>>> python
>>> from movies import db
>>> db.create_all()
```

In your terminal, run the following code to start your Flask server:
```
>>> python api.py
```

test the api using Postman, open the database with DBeaver to see the cars table and its data.

HTTP GET request => http://127.0.0.1:1234
```
{
    "success": true,
    "message": "our API works"
}
```


HTTP GET request => http://127.0.0.1:1234/cars
```
{
    "success": true,
    "cars": [
        {
            "id": 1,
            "make": "Porsche",
            "model": "718 Cayman GT4RS",
            "fuel_type": "petrol",
            "gearbox": "manual",
            "year": "2022-06-10 00:15:13"
        },
        {
            "id": 2,
            "make": "Porsche",
            "model": "911.992 GT3RS",
            "fuel_type": "petrol",
            "gearbox": "manual",
            "year": "2022-06-10 00:18:13"
        }
    ]
}
```



challenge: 
* lets find ways to refactor our api.py
* pull out Controller logic
* improve code by some error handling
* add a new child relationship to the Car ( like wheel for example ) or add an Owner and the car as its child relationship. 
* create a route/controller/model logic to be able to send a GET request to /cars/car_id_here/owner to get the owner record on a car record.
```
{
"success": true,
    "cars": [
        {
            "id": 1,
            "make": "Porsche",
            "model": "718 Cayman GT4RS",
            "fuel_type": "petrol",
            "gearbox": "manual",
            "year": "2022-06-10 00:15:13",
            "owner": {
                "id": 1,
                "name": "Magyar-Hunor Tamas",
                "email": "hunor@makers.tech"
            }
        }
}
```

