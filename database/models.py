from database.db import db

class usuarios(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))