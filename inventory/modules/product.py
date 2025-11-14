productos = []

class Producto:
    def __init__(self,
                fecha_registro,
                marca,
                modelo,
                tipo,
                talla,
                color,
                cantidad,
                precio_venta):

        self.codigo = len(productos) + 3001
        self.fecha_registro = fecha_registro
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.talla = talla
        self.color = color
        self.cantidad = cantidad
        self.precio_venta = precio_venta

        if 36 <= self.talla <= 39:
            self.genero = "dama"
        elif 40 <= self.talla <= 45:
            self.genero = "caballero"

        self.estado = "disponible" if self.cantidad > 0 else "agotado"

