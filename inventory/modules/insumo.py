insumos = []

#Clase de Insumos:
class Insumo:
    def __init__(self, nombre, categoria, unidad_medida, stock_actual, stock_minimo, fecha_registro, costo):
        self.codigo = len(insumos) + 1001
        self.nombre = nombre
        self.categoria = categoria
        self.unidad_medida = unidad_medida
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.fecha_registro = fecha_registro
        self.costo = costo
