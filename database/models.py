from database.db import db
from flask_login import UserMixin

class usuarios(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))