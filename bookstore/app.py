from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Make sure the URI points to the right location and is properly set up
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # This will use books.db in the same folder as your app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Turn off modification tracking to prevent warnings
db = SQLAlchemy(app)

# Define your models
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    grade = db.Column(db.String(50), nullable=False)
    cover_image = db.Column(db.String(100), nullable=False)
    pdf_file = db.Column(db.String(100), nullable=False)

# Run the following to create tables if they don't exist
with app.app_context():
    db.create_all()  # This will create the tables
