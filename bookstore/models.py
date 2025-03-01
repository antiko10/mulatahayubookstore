from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Admin model
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Book model
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    grade = db.Column(db.String(50), nullable=False)
    cover_image = db.Column(db.String(100), nullable=False)
    pdf_file = db.Column(db.String(100), nullable=False)
