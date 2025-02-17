from utils.db import db
from models.categorias import Categorias


class CategoriasQuery:
    @staticmethod
    def obtener_categorias():
        return Categorias.query.all()
        
    