# ============================================================================================
# IMPORTACIONES 
# ============================================================================================

from .modules.insumo import (
    Insumo,
    mostrar_alertas_stock,
    mostrar_resumen_alertas,
    insumos
)

from .modules.product import (
    Producto,
    consultar_insumos_produccion
)

from .modules.solicitud import (
    solicitar_insumos,
    gestionar_solicitudes_inventario
)

# ============================================================================================
# FUNCION: MENU DE INVENTARIO
# ============================================================================================

def menu_inventario():
    opciones = {
        "1": ("Registrar / Modificar Insumos.", Insumo.registrar_insumos),
        "2": ("Consultar Insumos.", Insumo.consultar_insumos),
        "3": ("Ver Alertas de Stock Bajo.", mostrar_alertas_stock),
        "4": ("Gestionar Solicitud de Insumos.", gestionar_solicitudes_inventario),
        "5": ("Salir del Sistema.", None)
    }

    while True:
        mostrar_resumen_alertas()

        print("\n" + "=" * 50)
        print("MÓDULO DE INVENTARIO")
        print("=" * 50)

        for clave, (desc, _) in opciones.items():
            print(f"{clave}. {desc}")

        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "5":
            print("\nSaliendo del módulo de Inventario...")
            break

        accion = opciones.get(opcion)
        if accion:
            funcion = accion[1]
            if funcion:
                funcion()
        else:
            print("Opción inválida.")

# ============================================================================================
# FUNCION: MENU DE PRODUCCION
# ============================================================================================

def menu_produccion():
    opciones = {
        "1": ("Registrar Productos.", Producto.registrar_productos),
        "2": ("Consultar Insumos.", consultar_insumos_produccion),
        "3": ("Solicitar Insumos.", lambda: solicitar_insumos(insumos)),
        "4": ("Salir del Sistema.", None)
    }

    while True:
        print("\n" + "=" * 50)
        print("MÓDULO DE PRODUCCIÓN")
        print("=" * 50)

        for clave, (desc, _) in opciones.items():
            print(f"{clave}. {desc}")

        print("=" * 50)

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "4":
            print("\nSaliendo del módulo de Producción...")
            break

        accion = opciones.get(opcion)
        if accion:
            funcion = accion[1]
            if funcion:
                funcion()
        else:
            print("Opción inválida.")
