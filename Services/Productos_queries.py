from utils.db import db
from models.productos import Productos
from flask import jsonify
from models.historial_cambios_productos import HistorialCambiosProducto

activo = 1
inactivo = 2    

class ProductosQuery:
    def obtener_productos():
        return Productos.query.filter_by(estado=activo).all()
    


    def crear_producto(valores_productos):
        producto = Productos(
            nombre=valores_productos["nombre"],
            descripcion=valores_productos["descripcion"],
            cantidad=valores_productos["cantidad"],
            precio=valores_productos["precio"],
            id_categoria=valores_productos["id_categoria"]
        )
        db.session.add(producto)
        db.session.commit()


    def actualizar_producto(valores_productos):
        producto = Productos.query.filter_by(id_producto=valores_productos["id_producto"]).first()

        if valores_productos["nombre"]:
            historial_n = HistorialCambiosProducto(id_producto= valores_productos["id_producto"], campo="nombre", valor_antiguo=producto.nombre, valor_nuevo=valores_productos["nombre"])
            producto.nombre = valores_productos["nombre"]
            db.session.add(historial_n)
        if valores_productos["descripcion"]:
            historial_d = HistorialCambiosProducto(id_producto= valores_productos["id_producto"], campo="descripcion", valor_antiguo=producto.descripcion, valor_nuevo=valores_productos["descripcion"])
            db.session.add(historial_d)
            producto.descripcion = valores_productos["descripcion"]
        if valores_productos["cantidad"]:
            historial_c = HistorialCambiosProducto(id_producto= valores_productos["id_producto"], campo="cantidad", valor_antiguo=producto.cantidad, valor_nuevo=valores_productos["cantidad"])
            db.session.add(historial_c)
            producto.cantidad = valores_productos["cantidad"]
        if valores_productos["precio"]:
            historial_p = HistorialCambiosProducto(id_producto= valores_productos["id_producto"], campo="precio", valor_antiguo=producto.precio, valor_nuevo=valores_productos["precio"])
            db.session.add(historial_p)
            producto.precio = valores_productos["precio"]
        if valores_productos["id_categoria"]:
            historial_i = HistorialCambiosProducto(id_producto= valores_productos["id_producto"], campo="id_categoria", valor_antiguo=producto.id_categoria, valor_nuevo=valores_productos["id_categoria"])
            db.session.add(historial_i)
            producto.id_categoria = valores_productos["id_categoria"]
        db.session.commit()

    @staticmethod
    def cambiar_estado_producto(valores_productos):
        producto = Productos.query.filter_by(id_producto=valores_productos["id_producto"]).first()
        historial = HistorialCambiosProducto(id_producto=valores_productos["id_producto"], campo="estado", valor_antiguo=producto.estado, valor_nuevo=valores_productos["estado"])
        db.session.add(historial)
        if producto.estado == activo:
            producto.estado = inactivo
        elif producto.estado == inactivo:
            producto.estado = activo
        db.session.commit()