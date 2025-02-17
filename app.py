from flask import Flask, session
from utils.db import db
from flask_cors import CORS
from routes.categorias import categorias

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "methods": ["GET", "POST", "PUT", "DELETE"], "allow_headers": ["Content-Type", "Authorization"]}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/alchemy_flask_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

db.init_app(app)

app.register_blueprint(categorias)
