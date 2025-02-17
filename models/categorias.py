from utils.db import db



class Categorias(db.Model):
    __tablename__ = 'categorias'

    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True) 
    estado = db.Column(db.Boolean, default=True, nullable=False)