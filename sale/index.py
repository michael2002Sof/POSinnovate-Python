# sale/index.py

from .modules.sale import registrar_venta
from .modules.voucher import generar_voucher
from .modules.seguimiento import consultar_estado_venta
from .modules.inventary_query import consultar_inventario_disponible

def sale_menu():
    while True:
        print("\n========= MÓDULO DE VENTAS =========")
        print("1. Registrar venta")
        print("2. Generar voucher")
        print("3. Consultar estado de venta")
        print("4. Consultar inventario disponible")
        print("5. Volver")
        print("====================================")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            generar_voucher()
        elif opcion == "3":
            consultar_estado_venta()
        elif opcion == "4":
            consultar_inventario_disponible()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.\n")
