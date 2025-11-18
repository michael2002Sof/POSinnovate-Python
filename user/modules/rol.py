class Rol:
    def __init__(self, name, modules=None, permissions=None):
        self.name = name
        self.modules = modules if modules else []
        self.permissions = permissions if permissions else []
        self.status = "Active"


    def __str__(self):
        return (
            f"Rol: {self.name} || "
            f"Modulos: {', '.join(self.modules)} || "
            f"Permisos: {', '.join(self.permissions)}"
        )