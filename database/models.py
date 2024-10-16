from database.db import db
from flask_login import UserMixin

class Usuarios(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    senha = db.Column(db.String(10))

class tarefas(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key = True)
    descrição = db.Column(db.String(255))
    data_lim = db.Column(db.String(8))
    status = db.column(db.Integer)
    usu_id = db.Column(db.Integer, db.ForeignKey('Usuarios.id'), nullable = False)

usuario = db.relationship('usuario', back_populates = 'tarefas')