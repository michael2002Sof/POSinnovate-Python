# sale/modules/sale.py

from datetime import datetime
import uuid

# ------------------------------
#   Clase DetalleVenta
# ------------------------------
class DetalleVenta:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto["precio"] * cantidad


# ------------------------------
#   Clase Venta
# ------------------------------
class Venta:
    def __init__(self, cliente):
        self.id_venta = str(uuid.uuid4())
        self.cliente = cliente  # diccionario con datos del cliente
        self.fecha = datetime.now()
        self.detalles = []
        self.total = 0

    def agregar_producto(self, producto, cantidad):
        if producto["stock"] < cantidad:
            print(f"Stock insuficiente para: {producto['nombre']}")
            return False
        
        # Descontar del inventario
        producto["stock"] -= cantidad

        detalle = DetalleVenta(producto, cantidad)
        self.detalles.append(detalle)
        self.total += detalle.subtotal
        return True

    def generar_factura(self):
        factura = {
            "id_venta": self.id_venta,
            "cliente": self.cliente,
            "fecha": str(self.fecha),
            "items": [
                {
                    "producto": d.producto["nombre"],
                    "cantidad": d.cantidad,
                    "precio": d.producto["precio"],
                    "subtotal": d.subtotal
                }
                for d in self.detalles
            ],
            "total": self.total
        }
        return factura


# ------------------------------
#   FUNCIÓN PÚBLICA DEL MÓDULO
# ------------------------------

def registrar_venta():
    print("\n--- Registrar Venta ---")

    cliente = {
        "nombre": input("Nombre del cliente: "),
        "direccion": input("Dirección del cliente: ")
    }

    # Ejemplo temporal de inventario (luego se conecta al módulo Inventario)
    inventario = {
        "P001": {"nombre": "Calzado Deportivo", "precio": 120000, "stock": 10},
        "P002": {"nombre": "Plantillas", "precio": 20000, "stock": 50}
    }

    venta = Venta(cliente)

    while True:
        codigo = input("\nCódigo del producto (o 0 para terminar): ")

        if codigo == "0":
            break

        if codigo not in inventario:
            print("El producto no existe.")
            continue

        cantidad = int(input("Cantidad: "))

        producto = inventario[codigo]

        venta.agregar_producto(producto, cantidad)

    factura = venta.generar_factura()

    print("\n✔ Venta registrada exitosamente")
    print(f"ID de la venta: {factura['id_venta']}")
    print(f"Total: {factura['total']}")

    print("\n--- Factura generada ---")
    for item in factura["items"]:
        print(f"- {item['producto']} x{item['cantidad']} = {item['subtotal']}")

    return factura
