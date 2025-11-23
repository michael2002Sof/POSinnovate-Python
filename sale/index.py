# sale/index.py

from .modules.voucher import VoucherManager
from .modules.sale import SaleManager
from .modules.seguimiento import SeguimientoManager
from .modules.inventary_query import InventarioManager


class MenuVentas:
    def __init__(self):
        self.voucher_manager = VoucherManager()
        self.sale_manager = SaleManager(self.voucher_manager)
        self.seguimiento_manager = SeguimientoManager(self.sale_manager)
        self.inventario_manager = InventarioManager()

    def run(self):
        while True:
            print("\n========= MÓDULO DE VENTAS =========")
            print("1. Registrar venta")
            print("2. Consultar estado de venta")
            print("3. Consultar inventario")
            print("4. Volver")
            print("====================================")

            opcion = input("Seleccione: ").strip()

            if opcion == "1":
                self.sale_manager.registrar_venta()

            elif opcion == "2":
                self.seguimiento_manager.consultar_estado_venta()

            elif opcion == "3":
                self.inventario_manager.consultar_disponibilidad()

            elif opcion == "4":
                break

            else:
                print("Opción inválida.\n")
