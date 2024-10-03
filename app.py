from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from routes.usuarios import usuario_route

app = Flask(__name__)
app.register_blueprint(usuario_route)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route("/")
def iniciar():
    return render_template('index.html')

with app.app_context():
    db.create_all()
app.run(debug= True)    