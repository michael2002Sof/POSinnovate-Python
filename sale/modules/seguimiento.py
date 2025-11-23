# sale/modules/seguimiento.py

class SeguimientoManager:
    def __init__(self, sale_manager):
        self.sale_manager = sale_manager

    def consultar_estado_venta(self):
        historial = self.sale_manager.historial_ventas

        if not historial:
            print("\n====================================================")
            print(" ¡NO HAY VENTAS REGISTRADAS EN EL SISTEMA!")
            print("====================================================\n")
            return

        while True:
            print("\n====================================================")
            print("      CONSULTA DE ESTADO DE VENTA (RF 3.3)")
            print("====================================================")
            print("1. Buscar por nombre del cliente")
            print("2. Buscar por código de voucher")
            print("3. Buscar por fecha")
            print("4. Volver")
            print("====================================================")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                nombre = input("Nombre del cliente: ").lower()
                resultados = [v for v in historial if v["cliente"].lower() == nombre]
                self._mostrar(resultados)

            elif opcion == "2":
                codigo = input("Código del voucher: ").strip()
                resultados = [v for v in historial if v["voucher_id"] == codigo]
                self._mostrar(resultados)

            elif opcion == "3":
                fecha = input("Fecha (DD/MM/AAAA): ").strip()
                resultados = [v for v in historial if v["fecha"] == fecha]
                self._mostrar(resultados)

            elif opcion == "4":
                break

            else:
                print("Opción inválida.\n")

    def _mostrar(self, resultados):
        if not resultados:
            print("\nNo se encontraron ventas.\n")
            return

        print("\n================ RESULTADOS ================\n")
        for v in resultados:
            print(f"Cliente: {v['cliente']}")
            print(f"Productos: {', '.join(v['productos'])}")
            print(f"Cantidad total: {v['cantidad_total']}")
            print(f"Total pagado: ${v['total']}")
            print(f"Fecha: {v['fecha']}")
            print(f"Estado: {v['estado']}")
            print(f"Voucher ID: {v['voucher_id']}")
            print("-------------------------------------------")
