from flask import Blueprint, request, jsonify
from Services.Categorias_query import CategoriasQuery


categorias = Blueprint('categorias', __name__)


@categorias.route('/categorias', methods=['GET'])
def obtener_Categorias():
    print("Accediendo a la ruta /categorias")
    categoria = CategoriasQuery.obtener_categorias()
    categorias_lista = [
        {
            'id_categoria': categoria.id_categoria,
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
            'estado': categoria.estado
        } for categoria in categoria
    ]
    return jsonify(categorias_lista), 200
