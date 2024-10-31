from flask import Blueprint, render_template, redirect, url_for,request, session
from database.models import Usuarios, tarefas
from database.db import db
from flask_login import login_user, logout_user, login_required, current_user

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

@app_route.route('/criar', methods = ['POST'])
@login_required
def criar_tarefa():  
        nova_tarefa = tarefas(nome = request.form['nome'],
                            descrição = request.form['desc'],
                            data = request.form['data'],
                            usu_id=current_user.id)
        db.session.add(nova_tarefa)
        db.session.commit()

        return redirect(url_for('iniciar'))
    
@app_route.route('/deletar/<id_tarefa>')
def deletar_tarefa(id_tarefa):
    id_tarefa = list(id_tarefa)
    id_tarefa = int(id_tarefa[9])

    tarefa = db.session.query(tarefas).filter_by(id=id_tarefa).first()

    db.session.delete(tarefa)
    db.session.commit()

    return redirect(url_for('iniciar'))

@app_route.route('/editar/<tarefa>' , methods = ['POST'])
def editar_tar(tarefa):
        id_tarefa = list(tarefa)
        id_tarefa = int(tarefa[9])

        tarefa = db.session.query(tarefas).filter_by(id=id_tarefa).first()

        tarefa.nome = request.form['nome']
        tarefa.descrição = request.form['desc']
        tarefa.data = request.form['data']

        db.session.commit()       

        return redirect(url_for('iniciar'))