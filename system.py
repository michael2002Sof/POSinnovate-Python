from access import login

from user.controllers.user import UserController
from user.controllers.rol import RolController

from user.models.user import User
from user.models.rol import Rol

class System:
    def __init__ (self):
        self.users = []             #Usuarios del sistema
        self.roles = []             #Roles del sistema
        self.product = []           #Productos del sistema
        self.supply = []            #Insumos del sistema
        self.requisitions = []     #Requisiciones del sistema
        self.sales = []             #Ventas del sistema

        #Modelos de clases
        self.model_user = User
        self.model_rol = Rol

        #Controladores
        self.controller_user = UserController(self)
        self.controller_rol = RolController(self)

        #Modulos del sistema
        self.AVAILABLE_MODULES = {
            "Usuarios": {
                "Crear Usuario": lambda: self.controller_user.create_user(),
                "Crear Admin" : lambda: self.controller_user.register_admin(),
                "Listar Usuarios": lambda : self.controller_user.list_users(),
                "Crear Rol": lambda : self.controller_rol.create_role()
            },
            "Inventario": {
                "Crear Producto": lambda: print("Funcion crear  producto en proceso..."),
                "Crear Insumo": lambda: print("Funcion crear  producto en proceso..."),
            },
            "Ventas": {
                "crear": lambda: print("Crear venta..."),
                "anular": lambda: print("Anular venta...")
            }
        }

# --------------------------------------------------------------
#                    EJECUCIÓN DEL SISTEMA
# --------------------------------------------------------------
if __name__ == "__main__":
    system = System()
    login(system)
