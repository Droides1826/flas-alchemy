from flask import Blueprint, request, jsonify
from services.Categorias_queries import CategoriasQuery


categorias = Blueprint('categorias', __name__)


@categorias.route('/categorias', methods=['GET'])
def obtener_Categorias():
    categoria = CategoriasQuery.obtener_categorias()
    categorias_lista = [
        {
            'nombre': categoria.nombre,
            'descripcion': categoria.descripcion,
            'id_categoria': categoria.id_categoria,
            
        } for categoria in categoria
    ]
    return jsonify(categorias_lista), 200

@categorias.route('/ingresar_categorias', methods=['POST'])
def ingresar_categoria():
    data = request.get_json()
    nombre = data.get('nombre')
    descripcion = data.get('descripcion')
    categoria = CategoriasQuery.crear_categoria(nombre, descripcion)
    return jsonify({
        'id_categoria': categoria.id_categoria,
        'nombre': categoria.nombre,
        'descripcion': categoria.descripcion,
        'estado': categoria.estado
    }), 201

