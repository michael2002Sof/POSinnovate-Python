# sale/index.py

from .modules.sale import sale_menu

def menu_principal_sale():
    while True:
        print("\n--- Módulo de Ventas ---")
        print("1. Registrar venta")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            sale_menu()
        elif option == "0":
            break
        else:
            print("Opción no válida.")
