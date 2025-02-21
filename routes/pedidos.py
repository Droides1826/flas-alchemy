from flask import Blueprint, request, jsonify
from services.pedidos_queries import PedidosQuery
from models.pedidos import Pedidos
from utils.Validaciones_pedidos import validacion_de_actualizar_estado_pedidos
from utils.respuestas import respuesta_json_fail

pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos', methods=['GET'])
def obtener_pedidos():
    pedidos = PedidosQuery.obtener_pedidos()
    pedidos_lista = [
        {
            'id_pedido': p.id_pedido,
            'id_producto': p.id_producto,
            'cantidad': p.cantidad,
            'estado': p.estado,
            'fecha': p.fecha_pedido
        } for p in pedidos
    ]
    return jsonify(pedidos_lista), 200

@pedidos.route('/cambiar_estado_pedidos', methods=['PUT'])
def cambiar_estado_pedido():
    try:
        valores_pedidos = {
            "id_pedido": request.json["id_pedido"],
            "estado": request.json["estado"]
        }
        
        validacion = validacion_de_actualizar_estado_pedidos(valores_pedidos)
        if validacion:
            return respuesta_json_fail(validacion, 400)

        error = PedidosQuery.cambiar_estado_pedido(valores_pedidos)
        if error:
            return jsonify({"error": error}), 400

        return jsonify("Estado cambiado con éxito"), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
