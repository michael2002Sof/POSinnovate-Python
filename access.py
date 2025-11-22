# --------------------------------------------------------------
#                  LOGIN PRINCIPAL
# --------------------------------------------------------------
from utils.system_utils import clean_screen
from menu import menu

def login(system):
    while True:
        clean_screen()
        print("\n=== SISTEMA POSInnovate ===")

        admin_exists = any(user.rol == "admin" for user in system.users)

        print("1. Iniciar sesión")
        if not admin_exists:
            print("2. Registrar Administrador (Primera vez)")
        print("0. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            clean_screen()
            print("\n=== Iniciar Sesion ===")

            email = input("Correo: ")
            password = input("Contraseña: ")

            user = next((u for u in system.users if u.email == email and u.password == password), None)
            
            if not user:
                print("\nUsuario no encontrado.")
                print("El administrador aún no le ha creado un usuario.\n")
                return


            # Abrir menú según rol
            role = next((r for r in system.roles if r.name == user.rol), None)
            clean_screen()
            menu(system, user, role)


        elif option == "2" and not admin_exists:
            clean_screen()
            system.controller_user.register_admin()

        elif option == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida\n")


