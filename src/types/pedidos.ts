export interface Pedidos {
    data: Data[]
    message: string
    status: number
    success: boolean
  }
  
  export interface Data{
    cantidad: number
    estado: number
    fecha: string
    id_pedido: number
    id_producto: number
  }
  