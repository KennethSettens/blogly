"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(20))
    LastName = db.Column(db.String(20))
    imageurl = db.Column(db.String) 
    
