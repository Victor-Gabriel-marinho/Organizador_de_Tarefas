from flask import Flask, render_template, session
from routes.usu import app_route, carrgar_tar
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from database.models import Usuarios, tarefas
from flask_login import LoginManager, current_user, login_required


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
@login_required
def iniciar():

    nome = session.get('nome')
    email = session.get('email')
    tarefas = carrgar_tar()

    return render_template('index.html', nome=nome, email=email, tarefas=tarefas)
    
#criando o banco de dados
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug= True)    