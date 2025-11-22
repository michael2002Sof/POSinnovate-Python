class RolController:
    def __init__(self, system):
        self.system = system

    # Registrar rol
    def create_role(self):
        print("\n--- Registrar Rol ---")
        name = input("Nombre del rol: ")

        # Mostrar módulos disponibles
        module_names = list(self.system.AVAILABLE_MODULES.keys())
        print("\nSeleccione módulos para este rol:")
        for i, mod in enumerate(module_names):
            print(f"{i+1}. {mod}")

        selected_modules = input(
            "Ingrese los números separados por coma (ej: 1,3): "
        ).split(",")

        modules_with_permissions = {}

        # Seleccionar módulos
        for index in selected_modules:
            index = index.strip()
            if index.isdigit():
                idx = int(index) - 1
                if 0 <= idx < len(module_names):
                    module_name = module_names[idx]
                    module_options = list(self.system.AVAILABLE_MODULES[module_name].keys())

                    # Mostrar permisos para el módulo
                    print(f"\nPermisos disponibles para '{module_name}':")
                    for i, perm in enumerate(module_options):
                        print(f"{i+1}. {perm}")

                    selected_perms = input(
                        f"Seleccione permisos para '{module_name}' separados por coma: "
                    ).split(",")

                    perms = []
                    for p in selected_perms:
                        p = p.strip()
                        if p.isdigit():
                            p_idx = int(p) - 1
                            if 0 <= p_idx < len(module_options):
                                perms.append(module_options[p_idx])

                    # Guardar módulo con sus permisos
                    modules_with_permissions[module_name] = perms

        # Crear rol
        new_role = self.system.model_rol(name, modules_with_permissions)
        self.system.roles.append(new_role)

        print(f"\n✓ Rol '{name}' registrado con éxito.\n")
        print(new_role)
