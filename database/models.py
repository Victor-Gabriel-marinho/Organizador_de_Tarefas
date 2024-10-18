from database.db import db
from flask_login import UserMixin

class Usuarios(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(10), nullable=False)
    tarefas = db.relationship('tarefas', backref = 'Usuarios', lazy = True)

class tarefas(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50), nullable = False)
    descrição = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Boolean, default=False)
    usu_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable = False)


