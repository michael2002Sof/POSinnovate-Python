solicitudes_insumos = []

# ============================================================================================
# CLASE SOLICITUD DE INSUMOS
# ============================================================================================

class SolicitudInsumo:
    def __init__(self, fecha_solicitud, responsable, items):
        self.codigo = len(solicitudes_insumos) + 5001
        self.fecha_solicitud = fecha_solicitud
        self.responsable = responsable
        self.estado = "pendiente"
        self.items = items

    def __str__(self):
        txt = [f"\nSolicitud #{self.codigo} - Fecha: {self.fecha_solicitud}",
               f"Responsable: {self.responsable} | Estado: {self.estado}",
               "Items solicitados:"]
        for item in self.items:
            insumo = item["insumo"]
            cantidad = item["cantidad"]
            txt.append(f"- {insumo.nombre} (cód {insumo.codigo}) → {cantidad} {insumo.unidad_medida}")
        return "\n".join(txt)

# =====================================================================
# SOLICITAR INSUMOS (RF 5.3)
# =====================================================================

def solicitar_insumos(lista_insumos):
    if not lista_insumos:
        print("\nNo hay insumos registrados.\n")
        return

    # Validar fecha
    while True:
        fecha_solicitud = input("Fecha solicitud (DD/MM/AAAA): ").strip()
        p = fecha_solicitud.split("/")
        if len(p) == 3 and all(x.isdigit() for x in p):
            d, m, a = map(int, p)
            if 1 <= d <= 31 and 1 <= m <= 12 and a >= 2025:
                break
        print("Fecha inválida.\n")

    responsable = input("Responsable: ").strip() or "Producción"
    items_solicitados = []

    while True:
        try:
            codigo = int(input("Código del insumo: "))
        except:
            print("Código inválido.\n")
            if input("¿Intentar otro? (SI/NO): ").lower() != "si":
                break
            else:
                continue

        insumo = next((i for i in lista_insumos if i.codigo == codigo), None)

        if not insumo:
            print("No encontrado.\n")
            if input("¿Intentar otro? (SI/NO): ").lower() != "si":
                break
            continue

        while True:
            try:
                cantidad = float(input("Cantidad solicitada: "))
                if cantidad > 0: break
            except: pass
            print("Cantidad inválida.\n")

        if cantidad > insumo.stock_actual:
            print(f"Advertencia: stock disponible = {insumo.stock_actual}\n")

        items_solicitados.append({"insumo": insumo, "cantidad": cantidad})

        if input("¿Agregar otro insumo? (SI/NO): ").lower() != "si":
            break

    if not items_solicitados:
        print("\nSolicitud sin items.\n")
        return

    solicitud = SolicitudInsumo(fecha_solicitud, responsable, items_solicitados)
    solicitudes_insumos.append(solicitud)

    print("\nSolicitud registrada correctamente.")
    print(solicitud)
    print("")


# =====================================================================
# GESTIONAR SOLICITUDES (INVENTARIO)
# =====================================================================

def obtener_solicitudes_pendientes():
    return [s for s in solicitudes_insumos if s.estado == "pendiente"]

def verificar_disponibilidad_solicitud(solicitud):
    faltantes = []
    for item in solicitud.items:
        if item["cantidad"] > item["insumo"].stock_actual:
            faltantes.append((item["insumo"], item["cantidad"] - item["insumo"].stock_actual))
    return faltantes

def gestionar_solicitudes_inventario():

    while True:
        pendientes = obtener_solicitudes_pendientes()

        if not pendientes:
            print("\nNo hay solicitudes pendientes.\n")
            break

        print("\nSolicitudes pendientes:")
        for s in pendientes:
            print(f"{s.codigo} | {s.fecha_solicitud} | {s.responsable} | Items: {len(s.items)}")

        try:
            codigo = int(input("\nCódigo a gestionar (0 para volver): "))
        except:
            print("Código inválido.\n")
            continue

        if codigo == 0:
            break

        solicitud = next((s for s in pendientes if s.codigo == codigo), None)

        if not solicitud:
            print("No encontrada.\n")
            continue

        print(solicitud)

        faltantes = verificar_disponibilidad_solicitud(solicitud)

        if faltantes:
            print("\nNo hay stock suficiente para aprobar:")
            for insumo, faltante in faltantes:
                print(f"- {insumo.nombre}: faltan {faltante}")
        else:
            print("\nStock suficiente para aprobar.\n")

        print("\nA = Aprobar | R = Rechazar | N = Nada\n")

        op = input("Opción: ").strip().lower()

        if op == "a":
            if faltantes:
                print("\nNo se puede aprobar.\n")
                continue

            for item in solicitud.items:
                item["insumo"].stock_actual -= item["cantidad"]

            solicitud.estado = "aprobada"
            print("\nSolicitud aprobada.\n")

        elif op == "r":
            solicitud.estado = "rechazada"
            print("\nSolicitud rechazada.\n")

        elif op == "n":
            print("\nSin cambios.\n")
