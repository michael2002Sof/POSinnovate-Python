from datetime import datetime
from .sale import historial_ventas   # Importamos el historial donde se guardan todas las ventas

# ===============================================================
# CONSULTAR ESTADO DE VENTA (RF 3.3)
# ===============================================================

def consultar_estado_venta():
    if not historial_ventas:
        print("\n====================================================")
        print(" ¡NO HAY VENTAS REGISTRADAS EN EL SISTEMA!")
        print("====================================================\n")
        return

    while True:
        print("\n====================================================")
        print("      CONSULTA DE ESTADO DE VENTA (RF 3.3)")
        print("====================================================")
        print("1. Buscar por nombre del cliente")
        print("2. Buscar por código de voucher")
        print("3. Buscar por fecha")
        print("4. Volver")
        print("====================================================")

        opcion = input("Seleccione una opción: ").strip()

        # --------------------------------------------------------
        # BUSCAR POR CLIENTE
        # --------------------------------------------------------
        if opcion == "1":
            nombre = input("\nNombre del cliente: ").strip().lower()
            resultados = [v for v in historial_ventas if v["cliente"].lower() == nombre]

            mostrar_resultados(resultados)

        # --------------------------------------------------------
        # BUSCAR POR CÓDIGO DE VOUCHER
        # --------------------------------------------------------
        elif opcion == "2":
            codigo = input("\nCódigo del voucher: ").strip()
            resultados = [v for v in historial_ventas if v["voucher_id"] == codigo]

            mostrar_resultados(resultados)

        # --------------------------------------------------------
        # BUSCAR POR FECHA
        # --------------------------------------------------------
        elif opcion == "3":
            fecha = input("\nIngrese la fecha (DD/MM/AAAA): ").strip()
            resultados = [v for v in historial_ventas if v["fecha"] == fecha]

            mostrar_resultados(resultados)

        elif opcion == "4":
            break
        else:
            print("Opción inválida.\n")


# ===============================================================
# FUNCIÓN PARA IMPRIMIR RESULTADOS
# ===============================================================

def mostrar_resultados(resultados):
    if not resultados:
        print("\nNo se encontraron ventas con ese criterio.\n")
        return

    print("\n================ RESULTADOS ================\n")
    for v in resultados:
        print(f"Cliente: {v['cliente']}")
        print(f"Producto(s): {', '.join(v['productos'])}")
        print(f"Total unidades: {v['cantidad_total']}")
        print(f"Precio total: ${v['total']}")
        print(f"Fecha: {v['fecha']}")
        print(f"Estado: {v['estado']}")
        print(f"Código voucher: {v['voucher_id']}")
        print("-------------------------------------------")
