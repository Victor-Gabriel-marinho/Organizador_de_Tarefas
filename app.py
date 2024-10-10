from flask import Flask, render_template
from routes.usu import app_route
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from flask_login import LoginManager, login_required


app = Flask(__name__)
#conectando com o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.register_blueprint(app_route)
lm = LoginManager(app)
app.secret_key= "qwe123"

@lm.user_loader
def save_user(id):
    usuario = db.session.query(usuario).filterby(id==id).first()
    return usuario

#inicializando o banco de dados
db.init_app(app)
  
@app.route("/")
@login_required
def iniciar():
    return render_template('index.html')

#criando o banco de dados
with app.app_context():
    db.create_all()
app.run(debug= True)    