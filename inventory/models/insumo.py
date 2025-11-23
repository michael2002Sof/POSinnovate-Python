from datetime import datetime

class Insumo:
    def __init__(self, codigo, nombre, unidad_medida, stock_actual, stock_minimo, costo, fecha_registro=None):
        self.codigo = codigo
        self.nombre = nombre
        self.unidad_medida = unidad_medida
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.costo = costo
        self.fecha_registro = fecha_registro or datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return (
            f"\n================================================================\n"
            f"Fecha: {self.fecha_registro}\n"
            f"Código: {self.codigo} | Nombre: {self.nombre}\n"
            f"Cantidad: {self.stock_actual} {self.unidad_medida} - Costo acumulado: ${self.costo}\n"
            "================================================================"
        )
