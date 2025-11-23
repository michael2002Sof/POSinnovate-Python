from utils.system_utils import clean_screen

def menu(system, user, role):
    clean_screen()
    print(f"\nBIENVENIDO: {user.name}. ROL: {role.name}")
    print("=" * 40)
    print("MENÚ DISPONIBLE")

    while True:

        modules = role.modules   # Diccionario: { "Usuarios": ["Crear Usuario",...] }
        print("MODULOS DISPONIBLES")
        print("=" * 40)
        for i, module in enumerate(modules.keys(), start=1):
            print(f"{i}. {module}")

        print("0. Cerrar sesión")
        print("=" *40)
        choice = input("Seleccione un módulo: ")

        if choice == "0":
            break

        try:
            module_name = list(modules.keys())[int(choice) - 1]
            permissions = modules[module_name]

            clean_screen()
            print("=" * 40)
            print(f"PERMISOS DEL MODULO {module_name}")
            print("=" * 40)

            # Mostrar acciones permitidas
            for j, perm in enumerate(permissions, start=1):
                print(f"{j}. {perm}")

            print("=" * 40)
            action = input("Seleccione acción: ")

            perm_name = permissions[int(action) - 1]

            clean_screen()
            print("=" * 50)
            print(f"EJECUTANDO '{perm_name}' EN MODULO '{module_name}'")
            print("=" * 50)
            # Ejecutar acción si existe
            action_function = system.AVAILABLE_MODULES[module_name].get(perm_name)

            if action_function:
                print()  # espacio visual
                action_function()
            else:
                print("Permiso no implementado o inexistente.")

        except Exception:
            print("Opción inválida.")
