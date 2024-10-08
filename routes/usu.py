from flask import Blueprint, render_template, redirect, url_for,request
from database.models import usuarios
from database.db import db
from flask_login import login_user, logout_user

app_route = Blueprint('usuario', __name__)

@app_route.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':

        return render_template('cadastro.html')
    
    elif request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        novo_usu = usuarios(email = email, senha = senha)
        db.session.add(novo_usu)
        db.session.commit()

        login_user(novo_usu)

        return redirect(url_for('iniciar'))
    
@app_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')
    
    elif request.method == "POST":
        email = request.form['email']
        senha = request.form['senha']

        user = db.session.query(usuarios).filter_by(email=email, senha=senha).first()
        if not user:
            return "este usuário não existe"
        
        login_user(user)
        return redirect(url_for('iniciar'))
    
@app_route.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))