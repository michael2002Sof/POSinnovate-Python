#=================================================================================================
# Clase SolicitudInsumo
#=================================================================================================

solicitudes_insumos = []

class SolicitudInsumo:
    def __init__(self, fecha_solicitud, responsable, items):
        self.codigo = len(solicitudes_insumos) + 5001
        self.fecha_solicitud = fecha_solicitud
        self.responsable = responsable
        self.estado = "pendiente"  # futura evolución: aprobada / rechazada / atendida
        self.items = items  # lista de diccionarios: {"insumo": obj_insumo, "cantidad": x}

    def __str__(self):
        texto = []
        texto.append(f"\nSolicitud #{self.codigo} - Fecha: {self.fecha_solicitud}")
        texto.append(f"Responsable: {self.responsable} | Estado: {self.estado}")
        texto.append("Insumos solicitados:")
        for item in self.items:
            insumo = item["insumo"]
            cantidad = item["cantidad"]
            texto.append(
                f"  - Código: {insumo.codigo} | Nombre: {insumo.nombre} | "
                f"Cantidad solicitada: {cantidad} {insumo.unidad_medida}"
            )
        return "\n".join(texto)

#=================================================================================================
# Solicitar insumos necesarios para producción  (RF 5.3)
#=================================================================================================

def solicitar_insumos(lista_insumos):
    if not lista_insumos:
        print("\nNo hay insumos registrados en inventario.\n")
        return

    # Fecha de la solicitud
    while True:
        fecha_solicitud = input("Ingrese la fecha de la solicitud (DD/MM/AAAA): ").strip()
        partes = fecha_solicitud.split("/")

        if len(partes) == 3:
            dia, mes, año = partes
            if dia.isdigit() and mes.isdigit() and año.isdigit():
                if len(dia) == 2 and len(mes) == 2 and len(año) == 4:
                    dia = int(dia)
                    mes = int(mes)
                    año = int(año)
                    if 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 2025:
                        break

        print("Fecha inválida. Debe estar en formato DD/MM/AAAA.\n")

    responsable = input("Nombre del responsable de producción: ").strip()
    if responsable == "":
        responsable = "Responsable de Producción"

    items_solicitados = []

    while True:
        print(" ")
        print("="*40)
        print("Agregar insumo a la solicitud")
        print("="*40)
        print(" ")

        # Buscar insumo por código
        try:
            codigo_insumo = int(input("Código del insumo a solicitar: ").strip())
        except ValueError:
            print("Código inválido.\n")
            continuar = input("¿Deseas intentar con otro insumo? (SI/NO): ").strip().lower()
            if continuar != "si":
                break
            else:
                continue

        insumo_encontrado = None
        for insumo in lista_insumos:
            if insumo.codigo == codigo_insumo:
                insumo_encontrado = insumo
                break

        if insumo_encontrado is None:
            print("No se encontró un insumo con ese código.\n")
            continuar = input("¿Deseas intentar con otro insumo? (SI/NO): ").strip().lower()
            if continuar != "si":
                break
            else:
                continue

        # Cantidad solicitada
        while True:
            cantidad_texto = input(
                f"Cantidad a solicitar de '{insumo_encontrado.nombre}': "
            ).strip()
            try:
                cantidad = float(cantidad_texto)
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser mayor que cero.\n")
            except ValueError:
                print("Cantidad inválida.\n")

        if cantidad > insumo_encontrado.stock_actual:
            print(
                f"ADVERTENCIA: estás solicitando {cantidad} {insumo_encontrado.unidad_medida}, "
                f"pero solo hay {insumo_encontrado.stock_actual} en inventario.\n"
            )

        items_solicitados.append(
            {"insumo": insumo_encontrado, "cantidad": cantidad}
        )

        continuar = input("¿Deseas agregar otro insumo a esta solicitud? (SI/NO): ").strip().lower()
        if continuar != "si":
            break

    if not items_solicitados:
        print("\nNo se registraron insumos en la solicitud.\n")
        return

    solicitud = SolicitudInsumo(fecha_solicitud, responsable, items_solicitados)
    solicitudes_insumos.append(solicitud)

    print("\nSolicitud registrada correctamente.")
    print(solicitud)
    print("")

#=================================================================================================
# Funciones de apoyo para Inventario: revisar / aprobar / rechazar solicitudes
#=================================================================================================

def obtener_solicitudes_pendientes():
    return [s for s in solicitudes_insumos if s.estado == "pendiente"]

def verificar_disponibilidad_solicitud(solicitud):

    faltantes = []
    for item in solicitud.items:
        insumo = item["insumo"]
        cantidad = item["cantidad"]
        if cantidad > insumo.stock_actual:
            faltante = cantidad - insumo.stock_actual
            faltantes.append((insumo, faltante))
    return faltantes

def gestionar_solicitudes_inventario():

    while True:
        pendientes = obtener_solicitudes_pendientes()

        if not pendientes:
            print("\nNo hay solicitudes de insumos pendientes.\n")
            break

        print("")
        print("=" * 60)
        print("Solicitudes de insumos pendientes")
        print("=" * 60)
        for solicitud in pendientes:
            print(
                f"Código: {solicitud.codigo} | Fecha: {solicitud.fecha_solicitud} | "
                f"Responsable: {solicitud.responsable} | Items: {len(solicitud.items)}"
            )
        print("=" * 60)
        print("Ingresa el código de la solicitud que deseas gestionar.")
        print("O escribe 0 para volver.\n")

        try:
            codigo_sel = int(input("Código de solicitud: ").strip())
        except ValueError:
            print("Código inválido.\n")
            continue

        if codigo_sel == 0:
            print("\nVolviendo al menú de Inventario...\n")
            break

        solicitud_seleccionada = None
        for solicitud in pendientes:
            if solicitud.codigo == codigo_sel:
                solicitud_seleccionada = solicitud
                break

        if solicitud_seleccionada is None:
            print("\nNo se encontró una solicitud pendiente con ese código.\n")
            continue

        # Mostrar detalle de la solicitud
        print(solicitud_seleccionada)

        # Verificar stock antes de aprobar
        faltantes = verificar_disponibilidad_solicitud(solicitud_seleccionada)
        if faltantes:
            print("\nNo hay stock suficiente para aprobar esta solicitud.")
            print("Faltantes detectados:")
            for insumo, faltante in faltantes:
                print(
                    f"- {insumo.nombre} (código {insumo.codigo}): faltan "
                    f"{faltante} {insumo.unidad_medida}"
                )
            print("\nPuedes rechazar la solicitud o dejarla pendiente.\n")
        else:
            print("\nHay stock suficiente para todos los insumos solicitados.\n")

        print("¿Qué deseas realizar con esta solicitud?")
        print("A = Aprobar")
        print("R = Rechazar")
        print("N = Regresar\n")

        accion = input("Opción (A/R/N): ").strip().lower()

        if accion == "a":
            if faltantes:
                print("\nNo se puede aprobar porque no hay stock suficiente.\n")
                continue

            # Descontar stock
            for item in solicitud_seleccionada.items:
                insumo = item["insumo"]
                cantidad = item["cantidad"]
                insumo.stock_actual -= cantidad

            solicitud_seleccionada.estado = "aprobada"

            print("\nSolicitud aprobada y stock actualizado correctamente.\n")

        elif accion == "r":
            solicitud_seleccionada.estado = "rechazada"
            print("\nSolicitud rechazada. No se realizaron cambios en el inventario.\n")

        elif accion == "n":
            print("\nNo se realizaron cambios en la solicitud.\n")

        else:
            print("\nOpción no válida. No se realizaron cambios.\n")
