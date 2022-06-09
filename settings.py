# importing libraries
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

# creating an instance of the flask app
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False # keep this in mind when you do this: https://stackoverflow.com/a/43263483

# Configure our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
