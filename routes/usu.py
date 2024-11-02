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
def carrgar_tar():

    tarefas_pen = tarefas.query.filter_by(usu_id=current_user.id, status = False).all()

    return tarefas_pen

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
    
@app_route.route('/deletar/<int:id_tar>')
def deletar_tarefa(id_tar):

    tarefa = db.session.query(tarefas).filter_by(id=id_tar).first()

    db.session.delete(tarefa)
    db.session.commit()

    return redirect(url_for('iniciar'))

@app_route.route('/editar/<int:id_tar>' , methods = ['POST'])
def editar_tar(id_tar):

        tarefa = db.session.query(tarefas).filter_by(id=id_tar).first()

        tarefa.nome = request.form['nome']
        tarefa.descrição = request.form['desc']
        tarefa.data = request.form['data']

        db.session.commit()       

        return redirect(url_for('iniciar'))

@app_route.route('/comp_tar/<int:tarefa_id>')
def completar_tar(tarefa_id):

    tarefa = db.session.query(tarefas).filter_by(id = tarefa_id).first()
    tarefa.status = True

    db.session.commit()

    return redirect(url_for('iniciar'))

@login_required
@app_route.route('/tar_completas')
def tar_completas():

    tar_comp = db.session.query(tarefas).filter_by(status = True, usu_id = current_user.id).all()

    return render_template('index.html',tarefas=tar_comp)