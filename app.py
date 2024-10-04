from flask import Flask, render_template
from routes.usu import app_route
from flask_sqlalchemy import SQLAlchemy
from database.db import db
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.register_blueprint(app_route)

db.init_app(app)
  
@app.route("/")
def iniciar():
    return render_template('index.html')

with app.app_context():
    db.create_all()
app.run(debug= True)    