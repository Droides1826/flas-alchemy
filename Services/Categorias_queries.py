from utils.db import db
from models.categorias import Categorias
from models.historial_cambios_categorias import HistorialCambiosCategoria
from flask import jsonify

activo = 1
inactivo = 2
class CategoriasQuery:
    
    @staticmethod
    def obtener_categorias():
        return Categorias.query.filter_by(estado=activo).all()
    
    @staticmethod
    def crear_categoria(valores_categorias):
        categoria = Categorias(nombre=valores_categorias["nombre"], descripcion=valores_categorias["descripcion"], estado=activo)
        db.session.add(categoria)
        db.session.commit()
        registro = HistorialCambiosCategoria(id_categoria=categoria.id_categoria, nombre=valores_categorias["nombre"], descripcion=valores_categorias["descripcion"], estado=activo) 
        db.session.add(registro)
        db.session.commit()

    
    @staticmethod
    def actualizar_categoria(valores_categorias):
        categoria = Categorias.query.filter_by(id_categoria=valores_categorias["id_categoria"]).first()
        if valores_categorias["nombre"]:
            categoria.nombre = valores_categorias["nombre"]
        if valores_categorias["descripcion"]:
            categoria.descripcion = valores_categorias["descripcion"]

        registro = HistorialCambiosCategoria(id_categoria=valores_categorias["id_categoria"], nombre=categoria.nombre, descripcion=categoria.descripcion, estado=categoria.estado)
        db.session.add(registro)
        
        db.session.commit()
    
    @staticmethod
    def cambiar_estado_categoria(valores_categorias):
        categoria = Categorias.query.filter_by(id_categoria=valores_categorias["id_categoria"]).first()
        registro = HistorialCambiosCategoria(id_categoria=valores_categorias["id_categoria"], nombre=categoria.nombre, descripcion=categoria.descripcion, estado=valores_categorias["estado"])
        if categoria.estado == activo:  
            categoria.estado = inactivo  
        elif categoria.estado == inactivo:  
            categoria.estado = activo
        db.session.add(registro)
        db.session.commit()
        
