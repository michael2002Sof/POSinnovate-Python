POSinnovate Python

    Este proyecto es una aplicación de consola desarrollada en Python, enfocada en el sistema
    POS (Point of Sale) que es la combinación de hardware y software que utilizan los negocios para completar las transacciones de venta con sus clientes, nuestro sistema toma apartir 
    de eso la base y lo impulsa mas haya creando modulos complemetarios, como inventario y 
    gestion de usuario, para mayor presencia en el mundo digital como sistema.


ARQUITECTURA MVC (Model – Controller – View simulada vía CLI)

POSINNOVATE-PYTHON/

    ├── main.py             → menú principal interactivo.
    ├── README.md           → explicación completa de la estructura y flujo del programa.

inventory/                  → Módulo de inventarios

    ├── Controllers/        
    |   ├── insumo.py       
    |   ├── product.py
    |   ├── solicitud.py
    └── Models
        └── insumo.py       → Modelo de Insumo
        └── product.py      → Modelo de Producto
        └── solicitud.py    → Modelo de Solicitud de Insumos


sale/                         → Módulo de ventas    

    ├── controllers/              → Controladores
    │   └── sale.py
    │
    └── models/                   → Modelos
        └── sale.py


finance/                      → Módulo de finanzas

    ├── controllers/              → Controladores
    │   └── finance.py
    │
    └── models/                   → Modelos
        └── movement.py


user/                       → Módulo de usuarios

    ├── Controllers        
        └── rol.py          → Lógica de roles del sistema
        └── user.py         → Lógica de gestión de usuarios
    └── Models
        └── rol.py
        └── user.py

utils/

    └── system_utils.py


División de Tareas

Michael Llanes
🔹 Product Owner / Developer 
🔹 Responsable del Módulo User

    * Gestión de usuarios
    * Control y asignación de roles
    * Creación, edición, eliminación y autenticación
    * Integración con módulos externos
    * Diseño del flujo principal desde perspectiva del producto

Brayan Casadiego
🔹 Scrum Master / Developer
🔹 Responsable del Módulo Inventory

    * Gestión de insumos
    * Gestión de productos
    * Control de solicitudes internas
    * Estructuración del flujo de inventario
    * Priorización del backlog y facilitación del equipo

RF 2 – Gestión de Inventario:

    * RF 2.1 – Registrar / Modificar Insumos

    Implementado en: InsumoController.registrar_insumos()
    Descripción corta:
    Permite registrar un nuevo insumo o actualizar uno existente.
    Valida unidad de medida, stock inicial, stock mínimo y costo.
    Si el insumo ya existe, permite aumentar cantidad y costo acumulado.
    Toda la información se almacena en system.supply.

    * RF 2.2 – Consultar Insumos

    Implementado en: InsumoController.consultar_insumos()
    Descripción corta:
    Permite buscar insumos por código, por nombre o mostrar todos.
    Usa la lista system.supply y muestra la información formateada del insumo.

    *RF 2.3 – Alertas de Stock Bajo

    Implementado en:
    InsumoController.mostrar_alertas_stock()
    InsumoController.mostrar_resumen_alertas()

    Descripción corta:
    Detecta insumos cuyo stock actual está por debajo del mínimo.
    Muestra alertas detalladas o un resumen de cuántos insumos están en riesgo.

    *RF 2.4 – Validar Salidas de Insumos (Producción)

    Implementado en:
    - SolicitudInsumo
    - Solicitar_insumos()
    - Gestionar_solicitudes_inventario()

    Producción solicita insumos y el inventario aprueba o rechaza.
    Si aprueba, descuenta stock de forma automática.
    Ningún insumo sale del inventario sin pasar por una solicitud validada.


RF 5 – Gestión de Producción:

    * RF 5.1 – Consultar disponibilidad de insumos

    Actor: Responsable de Producción
    Descripción breve:
    Permite consultar los insumos registrados en el inventario, buscando por código, nombre o mostrando todos.
    Implementación:
    Se utiliza consultar_insumos_produccion() del ProductController, que muestra el listado de insumos de system.supply.

    * RF 5.2 – Registrar nuevos productos

    Actor: Responsable de Producción
    Descripción breve:
    Registra productos fabricados (marca, modelo, tipo, talla, color, cantidad y precio).
    Implementación:
    El método registrar_productos() del ProductController permite registrar productos nuevos o actualizar existentes dentro de system.product.

    * RF 5.3 – Solicitar insumos para producción

    Actor: Responsable de Producción
    Descripción breve:
    Permite realizar solicitudes de insumos cuando producción necesita materiales.
    Implementación:
    El controlador SolicitudController gestiona:

    - Creación de solicitudes (solicitar_insumos()),
    - Registro de items solicitados,
    - Estado inicial pendiente en system.requisitions.



Daniel Palencia
🔹 Developer
🔹 Responsable de Módulo Finance y Sale

    * Controlador de ventas
    * Módulos de facturación
    * Registro de transacciones
    * Cálculo financiero (totales, impuestos, cierres)
    * Integración futura con módulo financiero completo
    * Gestión de métodos de pago
    * Reportes y estadísticas

RF 3 - Gestión de Ventas (Módulo Sale)

    * RF 3.1 – Registrar Venta
    - Registro completo de ventas desde el POS.
    - Valida disponibilidad de productos mediante el inventario.
    - Calcula subtotal, impuestos y total.
    - Descarga stock automáticamente al confirmar.

    * RF 3.2 – Generar Comprobante de Venta (Voucher)
    Genera un comprobante de venta con:
    - Productos vendidos
    - Método de pago
    - Totales
    - Fecha y datos relevantes

    Incluye visualización inmediata y almacenamiento interno.

    * RF 3.3 – Consultar Disponibilidad de Productos
    - Consulta en tiempo real del stock disponible.
    - Acceso directo a `system.product`.

    * RF 3.4 – Historial de Ventas
    - Lista completa de ventas realizadas.
    - Filtros por fecha, cliente, método de pago o vendedor.
    - Vista detallada de cada transacción.

    * RF 3.5 – Gestión de Métodos de Pago
    Soporte para:
    - Efectivo
    - Transferencia
    - Tarjeta
    - Pago mixto

    Registra internamente cada método y su transacción asociada.


RF 4 - Gestión Financiera (Módulo Finance)

    * RF 4.1 – Visualizar Transacciones Económicas
    - Lista de ingresos y egresos generados en el sistema.
    - Filtros avanzados por fecha, tipo o monto.

    * RF 4.2 – Reporte de Gastos
    - Registro detallado de gastos operativos.
    - Visualización por categoría, fecha y monto.

    * RF 4.3 – Reporte Financiero Completo
    Resumen general del estado financiero:
    - Ingresos totales
    - Egresos totales
    - Utilidad neta

Base para auditoría y análisis económico.

    * RF 4.4 – Historial de Pagos
    - Historial completo de pagos asociados a ventas.
    - Incluye método de pago, monto, estado y fecha.

    * RF 4.5 – Exportación de Datos
    Exportación a PDF y Excel de:
    - Transacciones
    - Gastos
    - Reportes financieros
