from flask import Blueprint, request, jsonify
from services.categorias_queries import categorias_queries
from utils.db import db
from models.categorias import Categoria

Categorias_bp = Blueprint('Categorias', __name__)

@Categorias_bp.route('/consultar_categorias', methods=['GET'])
def obtener_categorias():
    categorias = categorias_queries.obtener_categorias()
    categorias_json = [
        {
            "id_categoria": c.id_categoria,
            "nombre": c.nombre,
            "descripcion": c.descripcion,
            "estado": c.estado
        }
        for c in categorias
    ]
    return jsonify(categorias_json), 200
