class User:
    def __init__ (self, name, email, password, rol):
        self.name = name
        self.email = email
        self.password = password
        self.rol = rol
        self.status = "Active"
    
    def __str__(self):
        return f"Nombre: {self.name} || Correo: {self.email} || Contraseña: {self.password} || rol: {self.rol} || estado: {self.status}"
    



