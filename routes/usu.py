from flask import Blueprint, render_template, redirect, url_for,request
from database.models import usuarios
from app import db

usuario_route = Blueprint('usuarios', __name__)

@usuario_route.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('cadastro.html')
    elif request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        novo_usu = usuarios(email = email, senha = senha)
        db.session.add(novo_usu)
        db.session.commit()

        return redirect(url_for('inicio'))
    pass