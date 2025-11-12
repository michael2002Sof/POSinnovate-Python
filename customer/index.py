# customer/index.py

def customer_menu():
    while True:
        print("\n--- Módulo de Clientes ---")
        print("1. Registrar cliente")
        print("2. Listar clientes")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            print("Función para registrar cliente (próximamente).")
        elif option == "2":
            print("Función para listar clientes (próximamente).")
        elif option == "0":
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
