

# sale/index.py

def sale_menu():
    while True:
        print("\n--- Módulo de Ventas ---")
        print("1. Registrar venta")
        print("2. Registrar sucursal")
        print("3. Registrar punto de venta")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            print("Función para registrar venta (próximamente).")
        elif option == "2":
            print("Función para registrar sucursal (próximamente).")
        elif option == "3":
            print("Función para registrar punto de venta (próximamente).")
        elif option == "0":
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
