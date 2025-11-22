from utils.system_utils import clean_screen

def menu(system, user, role):
    clean_screen()
    print(f"\nBienvenido {user.name}. Rol: {role.name}")
    print("=== MENÚ DISPONIBLE ===")

    while True:

        modules = role.modules   # Diccionario: { "Usuarios": ["Crear Usuario",...] }

        print("\n--- Módulos disponibles ---")
        for i, module in enumerate(modules.keys(), start=1):
            print(f"{i}. {module}")

        print("0. Cerrar sesión")

        choice = input("\nSeleccione un módulo: ")

        if choice == "0":
            break

        try:
            module_name = list(modules.keys())[int(choice) - 1]
            permissions = modules[module_name]

            clean_screen()
            print(f"\n--- Permisos del modulo {module_name} ---")

            # Mostrar acciones permitidas
            for j, perm in enumerate(permissions, start=1):
                print(f"{j}. {perm}")

            action = input("Seleccione acción: ")

            perm_name = permissions[int(action) - 1]

            clean_screen()
            print(f"\n=== Ejecutando '{perm_name}' en módulo '{module_name}' ===")
            # Ejecutar acción si existe
            action_function = system.AVAILABLE_MODULES[module_name].get(perm_name)

            if action_function:
                print()  # espacio visual
                action_function()
            else:
                print("Permiso no implementado o inexistente.")

        except Exception:
            print("Opción inválida.")
