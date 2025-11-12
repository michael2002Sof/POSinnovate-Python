# user/index.py

def user_menu():
    while True:
        print("\n--- Módulo de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Registrar rol")
        print("3. Listar usuarios")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            print("Función para registrar usuario (próximamente).")
        elif option == "2":
            print("Función para registrar rol (próximamente).")
        elif option == "3":
            print("Función para listar usuarios (próximamente).")
        elif option == "0":
            break
        else:
            print("⚠️ Opción no válida. Intente nuevamente.")
