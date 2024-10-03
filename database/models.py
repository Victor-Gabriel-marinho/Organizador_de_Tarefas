from app import db

class usuarios(db.Model):

    id = db.column(db.Integer, primary_key = True)
    email = db.column(db.String(50), nullnable = False)
    senha = db.column(db.Sting(10), nullnable = False)