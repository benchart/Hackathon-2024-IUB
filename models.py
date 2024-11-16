from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    repository_name = db.Column(db.String(120), nullable=False)
    poc_id = db.Column(db.Integer, db.ForeignKey('contact.id'), nullable=False)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    chat_username = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='contact', lazy=True)