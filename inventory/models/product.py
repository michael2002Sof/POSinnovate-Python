from datetime import datetime

class Producto:
    def __init__(self, codigo, fecha_registro, marca, modelo, tipo, talla, color, cantidad, precio_venta):
        self.codigo = codigo
        self.fecha_registro = fecha_registro or datetime.now().strftime("%d/%m/%Y")
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
        else:
            self.genero = "no definido"

        self.estado = "disponible" if self.cantidad > 0 else "agotado"

    def __str__(self):
        return (
            f"\n================================================================\n"
            f"Fecha registro: {self.fecha_registro}\n"
            f"Código: {self.codigo}\n"
            f"Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.tipo}\n"
            f"Talla: {self.talla} | Color: {self.color} | Género: {self.genero}\n"
            f"Cantidad: {self.cantidad} par(es)\n"
            f"Precio unitario: ${self.precio_venta}\n"
            f"Estado: {self.estado}\n"
            f"================================================================"
        )
