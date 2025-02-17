from flask import Flask
from utils.db import db
from routes.categorias import Categorias_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'


db.init_app(app)

app.register_blueprint(Categorias_bp)
