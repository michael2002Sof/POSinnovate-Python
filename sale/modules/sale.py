# sale/modules/sale.py

from datetime import datetime
from inventory.modules.product import productos


class SaleManager:
    def __init__(self, voucher_manager):
        self.voucher_manager = voucher_manager
        self.historial_ventas = []

    def registrar_venta(self):
        print("\n====================================================")
        print("              REGISTRO DE VENTA (RF 3.1)")
        print("====================================================")

        if not productos:
            print("\nNO HAY PRODUCTOS REGISTRADOS EN INVENTARIO.\n")
            return

        carrito = []
        cantidades = []
        total = 0

        cliente = input("Nombre del cliente: ").strip()

        # -------------------------------
        # SELECCIÓN DE PRODUCTOS
        # -------------------------------
        while True:
            print("\n----- PRODUCTOS DISPONIBLES -----")
            for p in productos:
                print(f"{p.codigo} - {p.marca} {p.modelo} | Talla {p.talla} | "
                      f"${p.precio_venta} | Stock: {p.cantidad}")

            try:
                codigo = int(input("\nDigite el código del producto: "))
            except ValueError:
                print("Código inválido.\n")
                continue

            encontrado = next((p for p in productos if p.codigo == codigo), None)

            if not encontrado:
                print("Producto no encontrado.\n")
                continue

            # Cantidad
            try:
                cant = int(input("Cantidad a comprar: "))
            except:
                print("Cantidad inválida.\n")
                continue

            if cant <= 0 or cant > encontrado.cantidad:
                print("Cantidad no disponible.\n")
                continue

            carrito.append(encontrado)
            cantidades.append(cant)
            total += encontrado.precio_venta * cant

            otro = input("¿Agregar otro producto? (SI/NO): ").lower()
            if otro != "si":
                break

        # -------------------------------
        # REGISTRAR FECHA
        # -------------------------------
        fecha = datetime.now().strftime("%d/%m/%Y")

        # -------------------------------
        # GENERAR VOUCHER
        # -------------------------------
        voucher_id = self.voucher_manager.generar_voucher(
            cliente, carrito, cantidades, fecha, total
        )

        # -------------------------------
        # GUARDAR EN HISTORIAL
        # -------------------------------
        self.historial_ventas.append({
            "cliente": cliente,
            "productos": [f"{p.marca} {p.modelo}" for p in carrito],
            "cantidad_total": sum(cantidades),
            "total": total,
            "fecha": fecha,
            "estado": "en proceso",
            "voucher_id": voucher_id
        })

        print("\n====================================================")
        print("           ¡VENTA REGISTRADA CON ÉXITO!")
        print("====================================================")
        print(f"Total: ${total}")
        print(f"Voucher generado: {voucher_id}")
        print("====================================================\n")
