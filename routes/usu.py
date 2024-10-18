from flask import Blueprint, render_template, redirect, url_for,request, session
from database.models import Usuarios, tarefas
from database.db import db
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime

app_route = Blueprint('usuario', __name__)

@app_route.route('/cadastrar', methods = ['GET', 'POST'])
def cadastrar():
    if request.method == 'GET':

        return render_template('cadastro.html')
    
    elif request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        novo_usu = Usuarios(nome = nome, email = email, senha = senha)
        db.session.add(novo_usu)
        db.session.commit()

        login_user(novo_usu)

        session['nome'] = nome
        session['email'] = email

        return redirect(url_for('iniciar'))
    
@app_route.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':

        return render_template('login.html')
    
    elif request.method == "POST":
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        user = db.session.query(Usuarios).filter_by(nome=nome, email=email, senha=senha).first()
        if not user:
            return "este usuário não existe"
        
        login_user(user)

        session['nome'] = nome
        session['email'] = email

        return redirect(url_for('iniciar'))

@app_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('usuario.login'))

@login_required
def carrgar_tarefas():

    tarefas_usu = tarefas.query.filter_by(usu_id=current_user.id).all()

    return tarefas_usu

@login_required
def criar_tarefa():  
    if request.method == 'POST':
        nome = request.form['nome']
        desc = request.form['desc']
        data = request.form['data']

        da = datetime.now().strftime('%d-%m-%Y')
        if data != da:
            status = False
        elif data == da:
            status = True
        nova_tarefa = tarefas(nome =nome, descrição = desc, data=)