from flask import Flask, render_template, redirect,session
from routes.usu import app_route, carrgar_tarefas
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from database.models import Usuarios, tarefas
from flask_login import LoginManager, login_required


app = Flask(__name__)
#conectando com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.register_blueprint(app_route)
lm = LoginManager(app)
lm.login_view = "usuario.login"
app.secret_key= "qwe123"

@lm.user_loader
def save_user(id):
    usuario = db.session.query(Usuarios).filter_by(id=id).first()
    return usuario

#inicializando o banco de dados
db.init_app(app)
  
@app.route("/")
def iniciar():

    nome = session.get('nome')
    email = session.get('email')
    
    tarefas = carrgar_tarefas()  

    return render_template('index.html', nome=nome, email=email, tarefas=tarefas)

#criando o banco de dados
with app.app_context():
    db.create_all()
app.run(debug= True)    