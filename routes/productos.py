from flask import Blueprint, request, jsonify
from services.Productos_queries import ProductosQuery
from models.productos import Productos
from utils.Validaciones_productos import validaciones_ingresar_productos, cambiar_estado_productos
from utils.respuestas import respuesta_json_fail

productos = Blueprint('productos', __name__)

@productos.route('/productos', methods=['GET'])
def obtener_productos():
    producto = ProductosQuery.obtener_productos()
    productos_lista = [
        {
            'nombre': producto.nombre,
            'descripcion': producto.descripcion,
            'cantidad': producto.cantidad,
            'precio': producto.precio,
            'id_categoria': producto.id_categoria,
            'id_producto': producto.id_producto
        } for producto in producto
    ]
    return jsonify(productos_lista), 200

@productos.route('/ingresar_productos', methods=['POST'])
def ingresar_producto():
    try:
        valores_productos = {
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
            "cantidad": request.json["cantidad"],
            "precio": request.json["precio"],
            "id_categoria": request.json["id_categoria"]
        }
        validacion = validaciones_ingresar_productos(valores_productos)
        if validacion:
            return respuesta_json_fail(validaciones_ingresar_productos(valores_productos), 400)

        ProductosQuery.crear_producto(valores_productos)
        return jsonify("producto creado"), 200
    except Exception as e:
        return jsonify(str(e)), 400
    


@productos.route('/actualizar_productos', methods=['PUT'])
def actualizar_producto():
    try:
        valores_productos = {
            "id_producto": request.json["id_producto"],
            "nombre": request.json["nombre"],
            "descripcion": request.json["descripcion"],
            "cantidad": request.json["cantidad"],
            "precio": request.json["precio"]
           
        }
        ProductosQuery.actualizar_producto(valores_productos)
        return jsonify("producto actualizado"), 200
    except Exception as e:
        return jsonify(str(e)), 400
    

@productos.route('/cambiar_estado_productos', methods=['PUT'])
def cambiar_estado_producto():
    try:
        valores_productos = {
            "id_producto": request.json["id_producto"],
            "estado": request.json["estado"],
        }
        validacion = cambiar_estado_productos(valores_productos)
        if validacion:
            return respuesta_json_fail(validacion, 400)
            
        existe = ProductosQuery.cambiar_estado_producto(valores_productos)
        if  existe:
            return respuesta_json_fail("El producto no existe", 400)
        return jsonify(f"Estado del producto cambiado"), 200
    except Exception as e:
        return jsonify(str(e)), 400
