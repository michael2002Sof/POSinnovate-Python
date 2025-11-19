insumos = []

#=================================================================================================
# Clase de Insumos
#=================================================================================================

class Insumo:
    def __init__(self,
                 nombre,
                 unidad_medida,
                 stock_actual,
                 stock_minimo,
                 fecha_registro,
                 costo):

        self.codigo = len(insumos) + 1001
        self.nombre = nombre
        self.unidad_medida = unidad_medida
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.fecha_registro = fecha_registro
        self.costo = costo

#=============================================================================================
# Registro / Modificación de Insumo (RF 2.1)
#=============================================================================================
    def registrar_insumos():
        unidades_validas = ["litros", "metros", "unidad", "unidades"]

        while True:

            nombre_ = input("\nIngresa el nombre del insumo: ").strip().lower()

            # Buscar si ya existe
            insumo_existente = None
            for insumo in insumos:
                if insumo.nombre == nombre_:
                    insumo_existente = insumo
                    break

            # Caso 1: Insumo existente.
            if insumo_existente is not None:
                print(f"\nEl insumo '{nombre_}' ya se encuentra registrado.")

                while True:
                    opcion_2 = input("¿Desea modificar sus datos (Cantidad - Costo)? (SI/NO): ").strip().lower()

                    if opcion_2 == "si":
                        # Nueva cantidad
                        while True:
                            try:
                                cantidad_nueva = float(input("Ingrese la cantidad a agregar: "))
                                if cantidad_nueva >= 0:
                                    break
                                else:
                                    print("La cantidad no puede ser negativa.\n")
                            except ValueError:
                                print("Cantidad inválida.\n")

                        # Nuevo costo
                        while True:
                            costo_texto = input("Ingrese el costo a sumar: ").strip()
                            try:
                                costo_nuevo = float(costo_texto)
                                if costo_nuevo >= 0:
                                    break
                                else:
                                    print("El costo no puede ser negativo.\n")
                            except ValueError:
                                print("Costo inválido.\n")

                        # Actualizar insumo
                        insumo_existente.stock_actual += cantidad_nueva
                        insumo_existente.costo += costo_nuevo

                        print(" ")
                        print("="*40)
                        print("Insumo actualizado correctamente.")
                        print(f"Nuevo stock: {insumo_existente.stock_actual} {insumo_existente.unidad_medida}")
                        print(f"Nuevo costo acumulado: ${insumo_existente.costo}")
                        print("="*40)

                        # RF 2.3
                        mostrar_resumen_alertas()
                        break

                    elif opcion_2 == "no":
                        print("No se modificó el insumo.\n")
                        break
                    else:
                        print("Opción inválida.\n")

            # Caso 2: Nuevo Insumo.
            else:
                # Unidad medida
                while True:
                    unidad_medida_ = input("Ingrese la unidad de medida (Litros/Metros/Unidad/Unidades): ").strip().lower()
                    if unidad_medida_ in unidades_validas:
                        break
                    else:
                        print("Unidad no válida.\n")

                # Fecha
                while True:
                    fecha_registro_ = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
                    partes = fecha_registro_.split("/")

                    if len(partes) == 3:
                        dia, mes, año = partes
                        if dia.isdigit() and mes.isdigit() and año.isdigit():
                            if len(dia)==2 and len(mes)==2 and len(año)==4:
                                dia = int(dia)
                                mes = int(mes)
                                año = int(año)
                                if 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 2025:
                                    break

                    print("Fecha inválida.\n")

                # Stock inicial
                while True:
                    try:
                        stock_actual_ = float(input("Stock inicial: "))
                        if stock_actual_ >= 0:
                            break
                    except ValueError:
                        print("Cantidad inválida.\n")

                # Stock mínimo
                while True:
                    try:
                        stock_minimo_ = float(input("Stock mínimo: "))
                        if stock_minimo_ >= 0:
                            break
                    except ValueError:
                        print("Cantidad inválida.\n")

                # Costo inicial
                while True:
                    try:
                        costo_ = float(input("Costo inicial: "))
                        if costo_ >= 0:
                            break
                    except ValueError:
                        print("Costo inválido.\n")

                # Crear insumo
                insumo = Insumo(
                    nombre_,
                    unidad_medida_,
                    stock_actual_,
                    stock_minimo_,
                    fecha_registro_,
                    costo_
                )

                insumos.append(insumo)

                print(" ")
                print("="*40)
                print("Insumo registrado correctamente.")
                print("="*40)

                # RF 2.3
                mostrar_resumen_alertas()

            # Continuar o salir
            continuar = input("¿Deseas registrar otro insumo? (SI/NO): ").strip().lower()
            if continuar != "si":
                print("\nSaliendo del registro de insumos...\n")
                break

#=============================================================================================
# Consulta de Insumos (RF 2.2)
#=============================================================================================
    def consultar_insumos():
        if not insumos:

            print("="*40)
            print("\nNo hay insumos registrados.\n")
            print("="*40)

            return

        while True:

            print(" ")
            print("="*40)
            print("Consulta de Insumos")
            print("="*40)

            print("1. Buscar por código")
            print("2. Buscar por nombre")
            print("3. Ver todos")
            print("4. Volver\n")

            opcion = input("Selecciona una opción: ").strip()

            # Buscar por código
            if opcion == "1":
                try:
                    codigo_buscar = int(input("Ingresa el código: ").strip())
                except ValueError:
                    print("Código inválido.\n")
                    continue

                encontrado = False
                for insumo in insumos:
                    if insumo.codigo == codigo_buscar:
                        print(insumo)
                        encontrado = True
                        break

                if not encontrado:
                    print("\nNo se encontró un insumo con ese código.\n")

            # Buscar por nombre
            elif opcion == "2":
                nombre_buscar = input("Nombre: ").strip().lower()
                encontrados = [i for i in insumos if nombre_buscar in i.nombre]

                if encontrados:
                    for insumo in encontrados:
                        print(insumo)
                else:
                    print("\nNo se encontraron insumos.\n")

            # Ver todos
            elif opcion == "3":
                for insumo in insumos:
                    print(insumo)

            elif opcion == "4":
                break

            else:
                print("Opción no válida.\n")


    def __str__(self):
        return (
            f"\nFecha: {self.fecha_registro}\n"
            f"Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Cantidad: {self.stock_actual} {self.unidad_medida} | "
            f"Costo acumulado: ${self.costo}"
        )

#=================================================================================================
# Alertas por Bajo Stock (RF 2.3)
#=================================================================================================

def insumo_en_alerta(insumo):
    return insumo.stock_actual <= insumo.stock_minimo

def obtener_insumos_en_alerta():
    return [i for i in insumos if insumo_en_alerta(i)]

def mostrar_alertas_stock():
    alertas = obtener_insumos_en_alerta()

    if not alertas:
        print("\nNo hay insumos con stock bajo.\n")
        return

    print(" ")
    print("="*40)
    print("Alertas de Stock Bajo")
    print("="*40)

    for insumo in alertas:

        print(f"\n[ALERTA] Código: {insumo.codigo} | Nombre: {insumo.nombre}")
        print(f"Stock actual: {insumo.stock_actual} {insumo.unidad_medida}")
        print(f"Stock mínimo: {insumo.stock_minimo}")

        if insumo.stock_actual < insumo.stock_minimo:
            deficit = insumo.stock_minimo - insumo.stock_actual
            print(f"Faltan {deficit} {insumo.unidad_medida}.\n")

def mostrar_resumen_alertas():
    alertas = obtener_insumos_en_alerta()
    cantidad = len(alertas)

    if cantidad == 0:
        print("\nNo hay alertas de stock.\n")
    else:
        print(f"\nHay {cantidad} insumo(s) con stock bajo.")
        print("Revisa la opcion: Ver alertas de stock bajo.\n")


#=================================================================================================
# Menú Provicional
#=================================================================================================

def menu_inventario():
    while True:
        print("")
        print("="*40)
        print("Modulo de Inventario")
        print("="*40)

        print("1. Registrar / Modificar Insumo.")
        print("2. Consultar Insumos.")
        print("3. Ver alertas de stock bajo.")
        print("4. Volver\n")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            Insumo.registrar_insumos()
        elif opcion == "2":
            Insumo.consultar_insumos()
        elif opcion == "3":
            mostrar_alertas_stock()
        elif opcion == "4":
            print("\nVolviendo al menú principal...\n")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu_inventario()
