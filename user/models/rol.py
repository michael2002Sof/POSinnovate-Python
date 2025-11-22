class Rol:
    def __init__(self, name, modules=None):
        self.name = name
        self.modules = modules if modules else {}   # {"Usuarios":["Crear","Listar"], ...}
        self.status = "Active"

    def __str__(self):
        texto = f"Rol: {self.name}\nMódulos y permisos:\n"
        for module, perms in self.modules.items():
            permisos = ", ".join(perms)
            texto += f"  - {module}: {permisos}\n"
        return texto
