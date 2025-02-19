from flask import Blueprint, request, jsonify
from services.Categorias_queries import CategoriasQuery
from utils.Validaciones_categorias import validaciones_ingresar_categorias, si_existe_categoria, validaciones_actualizar_categorias, si_existe_categoria_por_id, validaciones_cambiar_estado_categorias
from utils.respuestas import respuesta_json_fail
from models.categorias import Categorias


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
    try:
        valores_categorias = {
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
        }
        validacion = validaciones_ingresar_categorias(valores_categorias)
        if validacion :
            return respuesta_json_fail(validaciones_ingresar_categorias(valores_categorias), 400)
        
        existe = si_existe_categoria(valores_categorias)
        if existe:
            return respuesta_json_fail("La categoría ya existe", 400)
        
        CategoriasQuery.crear_categoria(valores_categorias)
        return jsonify("categoria creada"), 200
    except Exception as e:
        return jsonify(str(e)), 400

@categorias.route('/actualizar_categorias', methods=['PUT'])	
def actualizar_categoria():
    try:
        valores_categorias = {
            "id_categoria": request.json["id_categoria"],
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
        }
        validacion = validaciones_actualizar_categorias(valores_categorias)
        if validacion:
            return respuesta_json_fail(validaciones_actualizar_categorias(valores_categorias), 400)
        
        existe = si_existe_categoria_por_id(valores_categorias)
        if not existe:
            return respuesta_json_fail("La categoría no existe", 400)
        
        CategoriasQuery.actualizar_categoria(valores_categorias)
        return jsonify("categoria actualizada"), 200
    except Exception as e:
        return jsonify(str(e)), 400
    

@categorias.route('/cambiar_estado_categorias', methods=['PUT'])
def cambiar_estado_categoria():
    try:
        valores_categorias = {
            "id_categoria": request.json["id_categoria"],
            "estado": request.json["estado"],
        }
        validacion = validaciones_cambiar_estado_categorias(valores_categorias)
        if validacion:
            return respuesta_json_fail(validacion, 400)
        
        existe = si_existe_categoria_por_id(valores_categorias)
        if not existe:
            return respuesta_json_fail("La categoría no existe", 400)
        
        CategoriasQuery.cambiar_estado_categoria(valores_categorias)
        return jsonify("Estado de la categoría cambiado"), 200
    except Exception as e:
        return jsonify(str(e)), 400
