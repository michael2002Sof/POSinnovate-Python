from .solicitud import solicitudes_insumos  # Importa solicitudes para verificar cuando inventario las revise

insumos = []

# ============================================================================================
# CLASE INSUMO
# ============================================================================================

class Insumo:
    def __init__(self, nombre, unidad_medida, stock_actual, stock_minimo, fecha_registro, costo):
        self.codigo = len(insumos) + 1001
        self.nombre = nombre
        self.unidad_medida = unidad_medida
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.fecha_registro = fecha_registro
        self.costo = costo

# ============================================================================================
# REGISTRO / MODIFICACIÓN DE INSUMO (RF 2.1)
# ============================================================================================

    def registrar_insumos():
        unidades_validas = ["litros", "metros", "unidad", "unidades"]

        while True:
            nombre_ = input("\nIngresa el nombre del insumo: ").strip().lower()

            # Verificar si existe
            insumo_existente = next((i for i in insumos if i.nombre == nombre_), None)

# ===================================================================
# SI EXISTE - MODIFICAR
# ===================================================================
            if insumo_existente is not None:
                print("=" * 40) 
                print("ADVERTENCIA:")
                print(f"El insumo '{nombre_}' ya está REGISTRADO.")
                print("=" * 40)

                while True:
                    opcion = input("\n¿Desea modificar cantidad y costo? (SI/NO): ").strip().lower()

                    if opcion == "si":
                        while True:
                            try:
                                cantidad_nueva = float(input("Cantidad a agregar: "))
                                if cantidad_nueva > 0:
                                    break
                                print("Cantidad inválida.\n")
                            except ValueError:
                                print("Cantidad inválida.\n")

                        while True:
                            try:
                                costo_nuevo = float(input("Costo a sumar: "))
                                if costo_nuevo > 0:
                                    break
                                print("Costo inválido.\n")
                            except ValueError:
                                print("Costo inválido.\n")

                        insumo_existente.stock_actual += cantidad_nueva
                        insumo_existente.costo += costo_nuevo

                        print("")
                        print("=" * 40) 
                        print("¡INSUMO ACTUALIZADO CORRECTAMENTE!")
                        print("=" * 40) 
                        print("")
                        break

                    elif opcion == "no":
                        print("¡NO SE MODIFICO EL INSUMO!.\n")
                        break

                cont = input("¿Registrar otro? (SI/NO): ").strip().lower()
                if cont != "si":
                    break
                continue

# ===================================================================
# NO EXISTE - REGISTRAR NUEVO
# ===================================================================

            while True:
                unidad_medida_ = input("Unidad de medida (Litros/Metros/Unidad/Unidades): ").strip().lower()
                if unidad_medida_ in unidades_validas:
                    break
                print("Unidad inválida, ingresa una unidad de medida permitida.\n")

            while True:
                fecha_registro_ = input("\nFecha (DD/MM/AAAA): ").strip()
                partes = fecha_registro_.split("/")
                if len(partes) == 3 and all(p.isdigit() for p in partes):
                    d, m, a = map(int, partes)
                    if 1 <= d <= 31 and 1 <= m <= 12 and a >= 2025:
                        break
                print("Fecha inválida.\n")

            while True:
                try:
                    stock_actual_ = float(input("Stock inicial: "))
                    if stock_actual_ > 0:
                        break
                    else:
                        print("El stock inicial debe ser mayor a 0.\n")
                except ValueError:
                    print("Cantidad inválida.\n")

            while True:
                try:
                    stock_minimo_ = float(input("Stock mínimo: "))
                    if stock_minimo_ > 0:
                        break
                    else:
                        print("El stock mínimo debe ser mayor a 0.\n")
                except ValueError:
                    print("Cantidad inválida.\n")

            while True:
                try:
                    costo_ = float(input("Costo inicial: "))
                    if costo_ > 0:
                        break
                    else:
                        print("El costo inicial debe ser mayor a 0.\n")
                except ValueError:
                    print("Costo inválido.\n")

            insumo = Insumo(nombre_, unidad_medida_, stock_actual_, stock_minimo_, fecha_registro_, costo_)
            insumos.append(insumo)

            print("")
            print("=" * 40)
            print("INSUMO REGISTRADO CORRECTAMENTE.")
            print("=" * 40)

            cont = input("\n¿Registrar otro? (SI/NO): ").strip().lower()
            if cont != "si":
                break

# ============================================================================================
# CONSULTA DE INSUMOS (RF 2.2)
# ============================================================================================

    def consultar_insumos():
        if not insumos:
            print("")
            print("=" * 40)
            print("¡NO HAY INSUMOS REGISTRADOS!")
            print("=" * 40)
            return

        while True:
            print("")
            print("=" * 40)
            print("CONSULTA DE INSUMOS")
            print("=" * 40)
            print("1. Buscar por código")
            print("2. Buscar por nombre")
            print("3. Ver todos")
            print("4. Volver")
            print("=" * 40)
            print("")

            opcion = input("Ingresa la opcion que deseas realizar: ").strip()

            if opcion == "1":
                try:
                    c = int(input("Código: "))
                except:
                    print("Código inválido.")
                    continue

                encontrado = next((i for i in insumos if i.codigo == c), None)

                if encontrado:
                    print(encontrado)
                else:
                    print("¡INSUMO NO ENCONTRADO!")

            elif opcion == "2":
                nombre = input("Nombre: ").strip().lower()
                encontrados = [i for i in insumos if nombre in i.nombre]

                if encontrados:
                    for i in encontrados:
                        print(i)
                else:
                    print("¡INSUMO NO ENCONTRADO!")

            elif opcion == "3":
                for i in insumos:
                    print(i)

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")

# ============================================================================================
# METODO DE IMPRESION
# ============================================================================================

    def __str__(self):
        return (
            f"\n================================================================\n"
            f"Fecha: {self.fecha_registro}\n"
            f"Código: {self.codigo} | Nombre: {self.nombre}\n"
            f"Cantidad: {self.stock_actual} {self.unidad_medida} - Costo acumulado: ${self.costo}\n"
            "================================================================"
        )

# ============================================================================================
# FUNCIONES DE ALERTAS (RF 2.3)
# ============================================================================================

def insumo_en_alerta(insumo):
    return insumo.stock_actual <= insumo.stock_minimo

def obtener_insumos_en_alerta():
    return [i for i in insumos if insumo_en_alerta(i)]

def mostrar_alertas_stock():
    alertas = obtener_insumos_en_alerta()

    if not alertas:
        print("")
        print("=" * 40)
        print("!NO HAY ALERTAS DE STOCK BAJO¡")
        print("=" * 40)
        return

    print("")
    print("=" * 40)
    print("ALERTAS DE STOCK BAJO")
    for i in alertas:
        print(f"[{i.codigo}] {i.nombre} | Stock: {i.stock_actual} / Mínimo: {i.stock_minimo}")
    print("=" * 40)

def mostrar_resumen_alertas():
    alertas = obtener_insumos_en_alerta()
    if alertas:
        print("")
        print("=" * 40)
        print(f"{len(alertas)} INSUMO(S) CON STOCK BAJO.")
        print("=" * 40)


