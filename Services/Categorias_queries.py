from utils.db import db
from models.categorias import Categorias

activo = 1
class CategoriasQuery:
    
    @staticmethod
    def obtener_categorias():
        return Categorias.query.filter_by(estado=activo).all()
    
    @staticmethod
    def crear_categoria(nombre, descripcion):
        categoria = Categorias(nombre=nombre, descripcion=descripcion)
        db.session.add(categoria)
        db.session.commit()
        return categoria
        
