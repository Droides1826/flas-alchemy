from utils.db import db
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, Numeric, DateTime, ForeignKey



db = SQLAlchemy()

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id_categoria = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    estado = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, nombre, descripcion=None, estado=1):
        self.nombre = nombre
        self.descripcion = descripcion
        self.estado = estado

    def to_dict(self):
        return {
            "id_categoria": self.id_categoria,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "estado": self.estado
        }
