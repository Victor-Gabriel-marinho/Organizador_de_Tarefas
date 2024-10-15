from database.db import db
from flask_login import UserMixin

class usuarios(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))

class tarefas(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    descrição = db.Column(db.String(255))
    data_lim = db.Column(db.String(8))
    status = db.column(db.Integer)