from access import login

# ------------------ USUARIOS ------------------
from user.controllers.user import UserController
from user.controllers.rol import RolController

from user.models.user import User
from user.models.rol import Rol

# ------------------ INVENTARIO ------------------
from inventory.Controllers.insumo import InsumoController
from inventory.Controllers.product import ProductController
from inventory.Controllers.solicitud import SolicitudController

class System:
    def __init__(self):

        #   LISTAS DEL SISTEMA
        self.users = []           # Usuarios del sistema
        self.roles = []           # Roles del sistema
        self.product = []         # Productos del sistema
        self.supply = []          # Insumos del sistema
        self.requisitions = []    # Requisiciones del sistema
        self.sales = []           # Ventas del sistema

        #   MODELOS (clases)
        self.model_user = User
        self.model_rol = Rol

        #   CONTROLADORES
        self.controller_user = UserController(self)
        self.controller_rol = RolController(self)

        self.controller_insumo = InsumoController(self)
        self.controller_product = ProductController(self)
        self.controller_solicitud = SolicitudController(self)

        # CARGUE DE INSUMOS, PRODUCTOS INICIALES
        self.controller_insumo.cargar_insumos_iniciales()
        self.controller_product.cargar_productos_iniciales()

        #   MÓDULOS DEL SISTEMA
        self.AVAILABLE_MODULES = {
            "Usuarios": {
                "Crear Usuario": lambda: self.controller_user.create_user(),
                "Crear Admin": lambda: self.controller_user.register_admin(),
                "Listar Usuarios": lambda: self.controller_user.list_users(),
                "Crear Rol": lambda: self.controller_rol.create_role(),
            },
            "Inventario": {
                "Crear Insumo": lambda: self.controller_insumo.registrar_insumos(),
                "Consultar Insumos": lambda: self.controller_insumo.consultar_insumos(),
                "Alertas de Stock": lambda: self.controller_insumo.mostrar_alertas_stock(),
                "Crear Producto": lambda: self.controller_product.registrar_productos(),
                "Consultar Insumos (Producción)": lambda: self.controller_product.consultar_insumos_produccion(),
                "Solicitar Insumos": lambda: self.controller_solicitud.solicitar_insumos(),
                "Gestionar Solicitudes": lambda: self.controller_solicitud.gestionar_solicitudes_inventario(),
            },
            "Ventas": {
                "crear": lambda: print("Crear venta..."),
                "anular": lambda: print("Anular venta..."),
            },
        }

# EJECUCIÓN DEL SISTEMA
if __name__ == "__main__":
    system = System()
    login(system)
