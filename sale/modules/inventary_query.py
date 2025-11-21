from ...inventory.modules.product import productos


# ===============================================================
# CONSULTAR DISPONIBILIDAD DE PRODUCTOS (RF 3.4)
# ===============================================================

def consultar_disponibilidad():
    if not productos:
        print("\n==============================================")
        print("   ¡NO HAY PRODUCTOS REGISTRADOS EN INVENTARIO!")
        print("==============================================\n")
        return

    while True:
        print("\n==============================================")
        print("      CONSULTA DE DISPONIBILIDAD (RF 3.4)")
        print("==============================================")
        print("1. Buscar por nombre (modelo)")
        print("2. Buscar por marca")
        print("3. Buscar por categoría (tipo)")
        print("4. Ver todos los productos")
        print("5. Volver")
        print("==============================================")

        opcion = input("Seleccione una opción: ").strip()

        # --------------------------------------------------------
        # BUSCAR POR MODELO (NOMBRE DEL PRODUCTO)
        # --------------------------------------------------------
        if opcion == "1":
            nombre = input("\nNombre o modelo del producto: ").strip().lower()
            resultados = [p for p in productos if nombre in p.modelo.lower()]
            mostrar_resultados(resultados)

        # --------------------------------------------------------
        # BUSCAR POR MARCA
        # --------------------------------------------------------
        elif opcion == "2":
            marca = input("\nMarca: ").strip().lower()
            resultados = [p for p in productos if p.marca.lower() == marca]
            mostrar_resultados(resultados)

        # --------------------------------------------------------
        # BUSCAR POR TIPO / CATEGORÍA
        # --------------------------------------------------------
        elif opcion == "3":
            tipo = input("\nCategoría / Tipo (deportivo, casual, formal, etc.): ").strip().lower()
            resultados = [p for p in productos if p.tipo.lower() == tipo]
            mostrar_resultados(resultados)

        # --------------------------------------------------------
        # MOSTRAR TODO EL INVENTARIO
        # --------------------------------------------------------
        elif opcion == "4":
            mostrar_resultados(productos)

        elif opcion == "5":
            break
        else:
            print("Opción inválida.\n")


# ===============================================================
# FUNCIÓN PARA IMPRIMIR RESULTADOS
# ===============================================================

def mostrar_resultados(lista):
    if not lista:
        print("\nNo se encontraron productos con ese criterio.\n")
        return

    print("\n================== RESULTADOS ==================\n")

    for p in lista:
        print(f"Código: {p.codigo}")
        print(f"Marca: {p.marca}")
        print(f"Modelo: {p.modelo}")
        print(f"Tipo: {p.tipo}")
        print(f"Talla: {p.talla}")
        print(f"Color: {p.color}")
        print(f"Cantidad disponible: {p.cantidad}")
        print(f"Precio: ${p.precio_venta}")
        print(f"Estado: {p.estado}")
        print("--------------------------------------------------")

    print("==================================================\n")
