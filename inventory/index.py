# inventory/index.py

def inventory_menu():
    while True:
        print("\n--- Módulo de Inventario ---")
        print("1. Registrar producto")
        print("2. Registrar insumo")
        print("3. Ver inventario general")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            print("Función para registrar producto (próximamente).")
        elif option == "2":
            print("Función para registrar insumo (próximamente).")
        elif option == "3":
            print("Función para mostrar inventario (próximamente).")
        elif option == "0":
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
