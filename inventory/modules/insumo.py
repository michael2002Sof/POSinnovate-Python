insumos = []

#=================================================================================================
#Clase de Insumos:
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

#=================================================================================================
#Registro / Modificación de Insumo (RF 2.1)
#=================================================================================================

    def registrar_insumos():
        unidades_validas = ["litros", "metros", "unidad", "unidades"]

        while True:  # permite registrar/modificar varios seguidos

            nombre_ = input("\nIngresa el nombre del insumo: ").strip().lower()

            #Buscar si ya existe
            insumo_existente = None
            for insumo in insumos:
                if insumo.nombre == nombre_:
                    insumo_existente = insumo
                    break

            #CASO 1: INSUMO EXISTENTE
            if insumo_existente is not None:
                print(f"\nEl insumo '{nombre_}' ya se encuentra registrado.")

                while True:
                    opcion_2 = input("¿Desea modificar sus datos (Cantidad - Costo)? (SI/NO): ").strip().lower()

                    if opcion_2 == "si":
                        #Nueva cantidad
                        while True:
                            try:
                                cantidad_nueva = float(input("Ingrese la cantidad a agregar: "))
                                if cantidad_nueva >= 0:
                                    break
                                else:
                                    print("La cantidad no puede ser negativa.\n")
                            except ValueError:
                                print("Cantidad inválida. Debe ser número.\n")

                        #Nuevo costo
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

                        #Actualizar insumo existente
                        insumo_existente.stock_actual += cantidad_nueva
                        insumo_existente.costo += costo_nuevo

                        print("\nInsumo actualizado correctamente.")
                        print(f"Nuevo stock: {insumo_existente.stock_actual} {insumo_existente.unidad_medida}")
                        print(f"Nuevo costo acumulado: ${insumo_existente.costo}\n")
                        break

                    elif opcion_2 == "no":
                        print("No se modificó el insumo.\n")
                        break
                    else:
                        print("Opción inválida, responde SI o NO.\n")

            #CASO 2: NUEVO INSUMO
            else:
                #Unidad de medida
                while True:
                    unidad_medida_ = input("Ingrese la unidad de medida (Litros/Metros/Unidad/Unidades): ").strip().lower()
                    if unidad_medida_ in unidades_validas:
                        break
                    else:
                        print("Unidad no válida, ingresa una unidad permitida.\n")

                #Fecha
                while True:
                    fecha_registro_ = input("Ingrese la fecha (DD/MM/AAAA): ").strip()
                    partes = fecha_registro_.split("/")

                    if len(partes) == 3:
                        dia, mes, año = partes

                        if dia.isdigit() and mes.isdigit() and año.isdigit():
                            if len(dia) == 2 and len(mes) == 2 and len(año) == 4:
                                dia = int(dia)
                                mes = int(mes)
                                año = int(año)

                                if 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 2025:
                                    break

                    print("Fecha inválida, inténtalo nuevamente.\n")

                #Cantidad
                while True:
                    try:
                        stock_actual_ = float(input("Stock inicial: "))
                        if stock_actual_ >= 0:
                            break
                        else:
                            print("La cantidad no puede ser negativa.\n")
                    except ValueError:
                        print("Debe ser número, inténtalo nuevamente.\n")

                #Stock mínimo
                while True:
                    try:
                        stock_minimo_ = float(input("Stock mínimo: "))
                        if stock_minimo_ >= 0:
                            break
                        else:
                            print("No puede ser negativo.\n")
                    except ValueError:
                        print("Debe ser número.\n")

                #Costo inicial
                while True:
                    costo_texto = input("Costo inicial: ").strip()
                    try:
                        costo_ = float(costo_texto)
                        if costo_ >= 0:
                            break
                        else:
                            print("Costo no puede ser negativo.\n")
                    except ValueError:
                        print("Debe ser número, inténtalo nuevamente.\n")

                #Crear insumo nuevo
                insumo = Insumo(
                    nombre_,
                    unidad_medida_,
                    stock_actual_,
                    stock_minimo_,
                    fecha_registro_,
                    costo_
                )

                insumos.append(insumo)
                print("\nInsumo registrado correctamente.\n")

            #Pregunta final para seguir o volver al menú
            continuar = input("¿Deseas registrar otro insumo? (SI/NO): ").strip().lower()
            if continuar != "si":
                print("\nSaliendo del registro de insumos...\n")
                break

#=================================================================================================
#Consulta de insumos (RF 2.2)
#=================================================================================================

    def consultar_insumos():
        if not insumos:
            print("\nNo hay insumos registrados en el inventario.\n")
            return

        while True:
            print("\n=== CONSULTA DE INSUMOS ===")
            print("1. Buscar por código")
            print("2. Buscar por nombre")
            print("3. Ver todos los insumos")
            print("4. Volver\n")

            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                try:
                    codigo_buscar = int(input("Ingresa el código del insumo: ").strip())
                except ValueError:
                    print("Código inválido.\n")
                    continue

                encontrado = False
                for insumo in insumos:
                    if insumo.codigo == codigo_buscar:
                        print("\nInsumo encontrado:")
                        print(insumo)
                        encontrado = True
                        break

                if not encontrado:
                    print("\nNo se encontró un insumo con ese código.\n")

            elif opcion == "2":
                nombre_buscar = input("Ingresa el nombre del insumo: ").strip().lower()
                encontrados = [i for i in insumos if nombre_buscar in i.nombre]

                if encontrados:
                    print("\nInsumos encontrados:")
                    for insumo in encontrados:
                        print(insumo)
                else:
                    print("\nNo se encontraron insumos con ese nombre.\n")

            elif opcion == "3":
                print("\nListado completo de insumos:")
                for insumo in insumos:
                    print(insumo)

            elif opcion == "4":
                print("\nVolviendo al menú principal...\n")
                break

            else:
                print("Opción no válida.\n")

    def __str__(self):
        return (
            f"\nFecha registro: {self.fecha_registro}\n"
            f"Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Cantidad: {self.stock_actual} {self.unidad_medida} | "
            f"Costo acumulado: ${self.costo}"
        )
    
#=================================================================================================

#Menú provisional
def menu_inventario():
    while True:
        print("\n===== MÓDULO DE INVENTARIO =====")
        print("1. Registrar / Modificar Insumo.")
        print("2. Consultar Insumos.")
        print("3. Salir\n")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            Insumo.registrar_insumos()

        elif opcion == "2":
            Insumo.consultar_insumos()

        elif opcion == "3":
            print("\nSaliendo del módulo de inventario...\n")
            break

        else:
            print("Opción no válida.\n")

menu_inventario()
