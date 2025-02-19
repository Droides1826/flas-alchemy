from flask import Flask
from utils.db import db
from routes.categorias import categorias

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/alchemy_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the SQLAlchemy instance with the app
db.init_app(app)

app.register_blueprint(categorias)
