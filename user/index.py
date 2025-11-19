# user/index.py
from modules.rol import Rol
from modules.user import User

class ManageUser: 
    def __init__(self):
        self.users = []
        self.roles = []

    # Módulos y permisos disponibles
    AVAILABLE_MODULES = [
        "Usuarios",
        "Productos",
        "Ventas",
        "Inventario",
        "Reportes",
        "Configuración",
    ]

    AVAILABLE_PERMISSIONS = [
        "Crear",
        "Leer",
        "Actualizar",
        "Eliminar",
    ]

    # Registrar usuario
    def register_user(self):
        if not self.roles:
            print("No hay roles registrados. Registre un rol primero.")
            return
        
        name = input("Nombre del usuario: ")
        email = input("Correo del usuario: ")
        password = input("Contraseña del usuario: ")

        print("\nSeleccione un rol:")
        for i, rol in enumerate(self.roles):
            print(f"{i+1}. {rol}")

        try:
            rol_index = int(input("Opción: ")) - 1
        except ValueError:
            print("Opción inválida.")
            return

        if rol_index < 0 or rol_index >= len(self.roles):
            print("Rol inválido.")
            return
        
        selected_role = self.roles[rol_index]
        user = User(name, email, password, selected_role.name)
        self.users.append(user)

        print(f"\n✓ Usuario '{name}' registrado correctamente\n")

    # Registrar rol
    def register_role(self):
        print("\n--- Registrar Rol ---")
        name = input("Nombre del rol: ")

        print("\nSeleccione módulos para este rol:")
        for i, mod in enumerate(self.AVAILABLE_MODULES):
            print(f"{i+1}. {mod}")

        selected_modules = input(
            "Ingrese los números separados por coma (ej: 1,3,5): "
        ).split(",")

        modules = []
        for index in selected_modules:
            index = index.strip()
            if index.isdigit():
                idx = int(index) - 1
                if 0 <= idx < len(self.AVAILABLE_MODULES):
                    modules.append(self.AVAILABLE_MODULES[idx])

        print("\nSeleccione permisos para este rol:")
        for i, perm in enumerate(self.AVAILABLE_PERMISSIONS):
            print(f"{i+1}. {perm}")

        selected_permissions = input(
            "Ingrese los números separados por coma (ej: 1,4): "
        ).split(",")

        permissions = []
        for index in selected_permissions:
            index = index.strip()
            if index.isdigit():
                idx = int(index) - 1
                if 0 <= idx < len(self.AVAILABLE_PERMISSIONS):
                    permissions.append(self.AVAILABLE_PERMISSIONS[idx])

        # Crear rol
        new_role = Rol(name, modules, permissions)
        self.roles.append(new_role)

        print(f"\n✓ Rol '{name}' registrado con éxito.")
        print(new_role)

    # Listar usuarios
    def list_users(self):
        if not self.users:
            print("No hay usuarios registrados.")
            return
        
        print("\n--- Lista de Usuarios ---")
        for u in self.users:
            print(u)

        # Registrar usuario ADMIN con todos los permisos
    def register_admin(self):
        print("\n--- Registrar Usuario Administrador ---")

        # Crear rol admin si no existe
        admin_role = None
        for r in self.roles:
            if r.name.lower() == "admin":
                admin_role = r
                break

        if not admin_role:
            admin_role = Rol(
                "admin",
                self.AVAILABLE_MODULES.copy(),   # Todos los módulos
                self.AVAILABLE_PERMISSIONS.copy()  # Todos los permisos
            )
            self.roles.append(admin_role)
            print("✓ Rol 'admin' creado automáticamente con todos los permisos.")

        # Datos del usuario admin
        name = input("Nombre del admin: ")
        email = input("Correo del admin: ")
        password = input("Contraseña del admin: ")

        # Crear usuario
        user = User(name, email, password, admin_role.name)
        self.users.append(user)

        print(f"\n✓ Usuario administrador '{name}' registrado correctamente\n")



def user_menu():
    manager = ManageUser()

    while True:
        print("\n--- Módulo de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Registrar rol")
        print("3. Listar usuarios")
        print("4. Registrar usuario admin")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            manager.register_user()

        elif option == "2":
            manager.register_role()

        elif option == "3":
            manager.list_users()
            
        elif option == "4":
            manager.register_admin()

        elif option == "0":
            break

        else:
            print("Opción no válida. Intente nuevamente.")


user_menu()
