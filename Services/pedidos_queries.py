from utils.db import db
from models.pedidos import Pedidos
from models.historia_cambios_pedidos import HistorialCambiosPedidos
from flask import jsonify

pendiente = 3
en_proceso = 4
entregado = 5
cancelado = 6

estado_nombres = {
    3: "pendiente",
    4: "en_proceso",
    5: "entregado",
    6: "cancelado"
}
class PedidosQuery:
    def obtener_pedidos():
        return Pedidos.query.all()
    
    def crear_pedido(valores_pedidos):
        pedido = Pedidos(
            fecha_pedido=valores_pedidos["fecha_pedido"],
            id_producto=valores_pedidos["id_producto"],
            cantidad=valores_pedidos["cantidad"],
            precio_unitario=valores_pedidos["precio_unitario"],
            estado=pendiente
        )
        db.session.add(pedido)
        db.session.commit()
        registro = Pedidos(id_pedido=pedido.id_pedido, fecha_pedido=pedido.fecha_pedido, id_producto=pedido.id_producto, cantidad=pedido.cantidad, precio_unitario=pedido.precio_unitario, estado=pendiente)
        db.session.add(registro)
        db.session.commit()             

    def cambiar_estado_pedido(valores_pedidos):
        pedido = Pedidos.query.filter_by(id_pedido=valores_pedidos["id_pedido"]).first()

        if not pedido:
            return "El pedido no existe"

        estado_actual = int(pedido.estado)  
        nuevo_estado = int(valores_pedidos["estado"])  

        transiciones_validas = {
            pendiente: [en_proceso, cancelado],
            en_proceso: [entregado, cancelado],
            entregado: [],
            cancelado: []
        }

        
        if nuevo_estado not in transiciones_validas.get(estado_actual, []):
            estado_actual_nombre = estado_nombres.get(estado_actual, estado_actual)
            nuevo_estado_nombre = estado_nombres.get(nuevo_estado, nuevo_estado)
            return f"No se puede cambiar el estado de {estado_actual_nombre} a {nuevo_estado_nombre}. Orden permitido: PENDIENTE → EN PROCESO → ENTREGADO/CANCELADO."

        pedido.estado = nuevo_estado  
        db.session.commit()
        
        return None

