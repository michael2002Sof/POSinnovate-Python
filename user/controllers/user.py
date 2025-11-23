class UserController:
    def __init__(self, system):
        self.system = system

    # Registrar usuario ADMIN con todos los permisos
    def register_admin(self):
        print("=" * 40)
        print("REGISTRO DE USUARIO ADMINISTRADOR")
        print("=" * 40)

        # ¿Existe el rol admin?
        admin_role = next((r for r in self.system.roles if r.name == "admin"), None)
                          
        if not admin_role:
            # Crear permisos completos para cada módulo
            full_permissions = {
                module: list(actions.keys())
                for module, actions in self.system.AVAILABLE_MODULES.items()
            }
            admin_role = self.system.model_rol("admin", full_permissions)
            self.system.roles.append(admin_role)
            print("Rol admin creado con todos los permisos.")

        # Datos del admin
        name = input("\nNombre del Admin: ")
        email = input("Correo del Admin: ")
        password = input("Contraseña del Admin: ")

        # Crear usuario
        user = self.system.model_user(name, email, password, admin_role.name)
        self.system.users.append(user)

        print(f"\nUSUARIO ADMINISTRADOR '{name}' REGISTRADO CORRECTAMENTE\n")

    # Registrar usuario
    def create_user(self):
        if not self.system.roles:
            print("!ADVERTENCIA¡ No hay roles registrados. Registre un rol primero.")
            return
        
        name = input("Nombre del usuario: ")
        email = input("Correo del usuario: ")
        password = input("Contraseña del usuario: ")

        print("=" * 40)
        print("SELECCION DE ROL:")
        print("=" * 40)
        for i, rol in enumerate(self.system.roles):
            print(f"{i+1}. {rol}")
        print("=" * 40)

        try:
            rol_index = int(input("Opción: ")) - 1
        except ValueError:
            print("Opción inválida.")
            return

        if rol_index < 0 or rol_index >= len(self.system.roles):
            print("Rol inválido.")
            return
        
        selected_role = self.system.roles[rol_index]
        user = self.system.model_user(name, email, password, selected_role.name)
        self.system.users.append(user)

        print(f"\n USUARIO '{name}' REGISTRADO CORRECTAMENTE\n")

    # Listar usuarios
    def list_users(self):
        if not self.system.users:
            print("No hay usuarios registrados.")
            return
        
        print("=" * 40)
        print("LISTA DE USUARIOS")
        print("=" * 40)
        for u in self.system.users:
            print(u)

