from datetime import datetime

from sale.models.sale import Sale, SaleItem


class SaleController:
    def __init__(self, system):
        self.system = system

    # ===============================================================
    # RF 3.1 - Registrar una venta de productos asociada a un cliente
    # (y RF 3.2 - Generar voucher al momento de registrar)
    # ===============================================================

    def registrar_venta(self):
        if not self.system.product:
            print("")
            print("=" * 60)
            print("¡NO HAY PRODUCTOS REGISTRADOS EN INVENTARIO!")
            print("=" * 60)
            return

        print("")
        print("=" * 60)
        print("REGISTRO DE VENTA")
        print("=" * 60)

        customer_name = input("Nombre del cliente: ").strip()
        if not customer_name:
            print("Nombre de cliente obligatorio. Venta cancelada.")
            return

        items = []

        while True:
            try:
                codigo = int(input("\nCódigo del producto (0 para finalizar): "))
            except ValueError:
                print("Código inválido.")
                continue

            if codigo == 0:
                break

            producto = next((p for p in self.system.product if p.codigo == codigo), None)

            if not producto:
                print("¡PRODUCTO NO ENCONTRADO!")
                continue

            if producto.cantidad <= 0:
                print("Producto sin stock disponible.")
                continue

            print(producto)  # muestra detalle del producto

            while True:
                try:
                    cantidad = int(input("Cantidad a vender: "))
                    if 0 < cantidad <= producto.cantidad:
                        break
                    else:
                        print(f"La cantidad debe estar entre 1 y {producto.cantidad}.")
                except ValueError:
                    print("Cantidad inválida.")

            # crear item de venta con el precio actual del producto
            item = SaleItem(producto, cantidad, producto.precio_venta)
            items.append(item)

            # ¿Agregar otro producto?
            mas = input("¿Agregar otro producto? (SI/NO): ").strip().lower()
            if mas != "si":
                break

        if not items:
            print("\nNo se agregaron productos. Venta cancelada.\n")
            return

        print("")
        print("FORMA DE PAGO")
        print("1. Efectivo")
        print("2. Transferencia")
        print("3. Tarjeta")
        opcion_pago = input("Opción: ").strip()

        if opcion_pago == "1":
            payment_method = "Efectivo"
        elif opcion_pago == "2":
            payment_method = "Transferencia"
        elif opcion_pago == "3":
            payment_method = "Tarjeta"
        else:
            payment_method = "No especificado"

        code = len(self.system.sales) + 7001
        date = datetime.now().strftime("%d/%m/%Y %H:%M")

        venta = Sale(code, date, customer_name, items, payment_method)

        # Descontar stock de productos
        for item in items:
            item.product.cantidad -= item.quantity
            item.product.estado = "disponible" if item.product.cantidad > 0 else "agotado"

        self.system.sales.append(venta)

        print("")
        print("=" * 60)
        print("¡VENTA REGISTRADA CORRECTAMENTE!")
        print("=" * 60)

        # RF 3.2 - Mostrar voucher automáticamente
        self.mostrar_voucher(venta)

    def mostrar_voucher(self, venta):
        print("")
        print(venta)

    # ===============================================================
    # RF 3.3 - Consultar disponibilidad de productos en inventario
    # (igual estilo que ver insumos)
    # ===============================================================

    def consultar_productos_disponibles(self):
        if not self.system.product:
            print("")
            print("=" * 40)
            print("¡NO HAY PRODUCTOS REGISTRADOS!")
            print("=" * 40)
            return

        while True:
            print("")
            print("=" * 40)
            print("CONSULTA DE PRODUCTOS")
            print("=" * 40)
            print("1. Buscar por código")
            print("2. Buscar por marca/modelo/tipo")
            print("3. Ver todos")
            print("4. Volver")
            print("=" * 40)
            print("")

            opcion = input("Opción: ").strip()

            if opcion == "1":
                try:
                    c = int(input("Código del producto: "))
                except ValueError:
                    print("Código inválido.")
                    continue

                encontrado = next((p for p in self.system.product if p.codigo == c), None)

                if encontrado:
                    print(encontrado)
                else:
                    print("¡PRODUCTO NO ENCONTRADO!")

            elif opcion == "2":
                texto = input("Texto a buscar (marca/modelo/tipo): ").strip().lower()
                encontrados = [
                    p for p in self.system.product
                    if texto in p.marca
                    or texto in p.modelo
                    or texto in p.tipo
                ]

                if encontrados:
                    for p in encontrados:
                        print(p)
                else:
                    print("¡NO SE ENCONTRARON PRODUCTOS!")

            elif opcion == "3":
                for p in self.system.product:
                    print(p)

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")