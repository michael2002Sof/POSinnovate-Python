from datetime import datetime
from ..models.insumo import Insumo

class InsumoController:
    def __init__(self, system):
        self.system = system

# ============================================================================================
# REGISTRO / MODIFICACIÓN DE INSUMO (RF 2.1)
# ============================================================================================

    def registrar_insumos(self):
        unidades_validas = ["litros", "metros", "unidad", "unidades"]

        while True:
            nombre_ = input("\nIngresa el nombre del insumo: ").strip().lower()

            # Verificar si existe
            insumo_existente = next(
                (i for i in self.system.supply if i.nombre == nombre_), None
            )

# ===================================================================
# SI EXISTE - MODIFICAR
# ===================================================================

            if insumo_existente is not None:
                print("=" * 40)
                print("ADVERTENCIA:")
                print(f"El insumo '{nombre_}' ya está REGISTRADO.")
                print("=" * 40)

                while True:
                    opcion = input(
                        "\n¿Desea modificar cantidad y costo? (SI/NO): "
                    ).strip().lower()

                    if opcion == "si":
                        while True:
                            try:
                                cantidad_nueva = float(
                                    input("Cantidad a agregar: ")
                                )
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

                        # Registrar gasto LIMPIO
                        if hasattr(self.system, "controller_finance"):
                            self.system.controller_finance.registrar_gasto_insumo(
                                insumo_existente,
                                costo_nuevo
                            )

                        print("")
                        print("=" * 40)
                        print("¡INSUMO ACTUALIZADO CORRECTAMENTE!")
                        print("=" * 40)
                        print("")
                        break

                    elif opcion == "no":
                        print("¡NO SE MODIFICO EL INSUMO!.\n")
                        break

                    else:
                        print("Opción inválida. Responda SI o NO.\n")

                cont = input("¿Registrar otro? (SI/NO): ").strip().lower()
                if cont != "si":
                    break
                continue

# ===================================================================
# NO EXISTE - REGISTRAR NUEVO
# ===================================================================

            while True:
                unidad_medida_ = input(
                    "Unidad de medida (Litros/Metros/Unidad/Unidades): "
                ).strip().lower()
                if unidad_medida_ in unidades_validas:
                    break
                print(
                    "Unidad inválida, ingresa una unidad de medida permitida.\n"
                )

            fecha_registro_ = datetime.now().strftime("%d/%m/%Y")
            print(f"\nFecha de Registro: {fecha_registro_}")

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
                    print("Costo inválida.\n")

            codigo = len(self.system.supply) + 1001
            insumo = Insumo(
                codigo,
                nombre_,
                unidad_medida_,
                stock_actual_,
                stock_minimo_,
                costo_,
                fecha_registro_,
            )
            self.system.supply.append(insumo)

            # Registrar gasto LIMPIO
            if hasattr(self.system, "controller_finance"):
                self.system.controller_finance.registrar_gasto_insumo(
                    insumo,
                    costo_
                )

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

    def consultar_insumos(self):
        if not self.system.supply:
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

            opcion = input(
                "Ingresa la opcion que deseas realizar: "
            ).strip()

            if opcion == "1":
                try:
                    c = int(input("Código: "))
                except ValueError:
                    print("Código inválido.")
                    continue

                encontrado = next(
                    (i for i in self.system.supply if i.codigo == c), None
                )

                if encontrado:
                    print(encontrado)
                else:
                    print("¡INSUMO NO ENCONTRADO!")

            elif opcion == "2":
                nombre = input("Nombre: ").strip().lower()
                encontrados = [
                    i
                    for i in self.system.supply
                    if nombre in i.nombre
                ]

                if encontrados:
                    for i in encontrados:
                        print(i)
                else:
                    print("¡INSUMO NO ENCONTRADO!")

            elif opcion == "3":
                for i in self.system.supply:
                    print(i)

            elif opcion == "4":
                break

            else:
                print("Opción inválida.")

# ============================================================================================
# FUNCIONES DE ALERTAS (RF 2.3)
# ============================================================================================

    def mostrar_alertas_stock(self):
        alertas = [
            i
            for i in self.system.supply
            if i.stock_actual <= i.stock_minimo
        ]

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
            print(
                f"[{i.codigo}] {i.nombre} | Stock: {i.stock_actual} / Mínimo: {i.stock_minimo}"
            )
        print("=" * 40)

    def mostrar_resumen_alertas(self):
        alertas = [
            i
            for i in self.system.supply
            if i.stock_actual <= i.stock_minimo
        ]
        if alertas:
            print("")
            print("=" * 40)
            print(f"{len(alertas)} INSUMO(S) CON STOCK BAJO.")
            print("=" * 40)

# =====================================================================
# INSUMOS REGISTRADOS DE FORMA INICIAL
# =====================================================================

    def cargar_insumos_iniciales(self):
        if self.system.supply:
            return

        fecha_hoy = datetime.now().strftime("%d/%m/%Y")

        def crear_insumo_inicial(nombre, unidad, stock, minimo, costo):
            codigo = len(self.system.supply) + 1001
            insumo = Insumo(
                codigo,
                nombre,
                unidad,
                stock,
                minimo,
                costo,
                fecha_hoy,
            )
            self.system.supply.append(insumo)

            # Registrar gasto LIMPIO
            if hasattr(self.system, "controller_finance"):
                self.system.controller_finance.registrar_gasto_insumo(
                    insumo,
                    costo
                )

        crear_insumo_inicial("super", "litros", 40, 5, 75000)
        crear_insumo_inicial("suelas", "unidades", 80, 10, 48000)
        crear_insumo_inicial("malla", "metros", 50, 8, 90000)
