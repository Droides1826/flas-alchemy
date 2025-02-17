from utils.db import db
from models.categorias import Categoria
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

class categorias_queries:
    @staticmethod
    def obtener_categorias():
        return Categoria.query.all()

    @staticmethod
    def ingresar_categoria(nombre, descripcion):
        nueva_categoria = Categoria(
            nombre=nombre,
            descripcion=descripcion
        )
        
        db.session.add(nueva_categoria)
        db.session.commit()
        return nueva_categoria
         
    @staticmethod
    def actualizar_categoria(id, nombre, descripcion):
        categoria = Categoria.query.get(id)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        
        categoria.nombre = nombre
        categoria.descripcion = descripcion
        
        db.session.commit()
        return jsonify(categoria)
    
    @staticmethod
    def cambiar_categoria_a_inactivo(id):
        categoria = Categoria.query.get(id)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        
        categoria.estado = 'inactivo'
        db.session.commit()
        return jsonify(categoria)
    
    @staticmethod
    def cambiar_categoria_a_activo(id):
        categoria = Categoria.query.get(id)
        if not categoria:
            return jsonify({'error': 'Categoria no encontrada'}), 404
        
        categoria.estado = 'activo'
        db.session.commit()
        return jsonify(categoria)