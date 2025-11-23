from datetime import datetime
from inventory.models.solicitud import SolicitudInsumo

class SolicitudController:
    def __init__(self, system):
        self.system = system

# =====================================================================
# SOLICITAR INSUMOS (RF 5.3)
# =====================================================================

    def solicitar_insumos(self):
        if not self.system.supply:
            print("")
            print("=" * 40)
            print("¡NO HAY INSUMOS REGISTRADOS!")
            print("=" * 40)
            return

        fecha_solicitud = datetime.now().strftime("%d/%m/%Y")
        print(f"\nFecha de Registro: {fecha_solicitud}")

        responsable = input("Responsable: ").strip() or "Producción"
        items_solicitados = []

        while True:
            try:
                codigo = int(input("Código del insumo: "))
            except ValueError:
                print("Código inválido.\n")
                if (
                    input("¿Intentar otro? (SI/NO): ").lower()
                    != "si"
                ):
                    break
                else:
                    continue

            insumo = next(
                (i for i in self.system.supply if i.codigo == codigo),
                None,
            )

            if not insumo:
                print("!TU CODIGO DE INSUMO, NO FUE ENCONTRADO¡\n")
                if (
                    input(
                        "¿Deseas intentar nuevamente? (SI/NO): "
                    ).lower()
                    != "si"
                ):
                    break
                continue

            while True:
                try:
                    cantidad = float(
                        input("Cantidad solicitada: ")
                    )
                    if cantidad > 0:
                        break
                    else:
                        print(
                            "La cantidad debe ser mayor a 0.\n"
                        )
                except ValueError:
                    print(
                        "Cantidad inválida, ingresa un número válido.\n"
                    )

            if cantidad > insumo.stock_actual:
                print("=" * 40)
                print("ADVERTENCIA DE STOCK")
                print(f"Stock disponible: {insumo.stock_actual}")
                print(
                    f"Cantidad solicitada: {cantidad} (NO DISPONIBLE)"
                )
                print("=" * 40)

            items_solicitados.append(
                {"insumo": insumo, "cantidad": cantidad}
            )

            if (
                input(
                    "\n¿Deseas agregar otro insumo? (SI/NO): "
                ).lower()
                != "si"
            ):
                break

        if not items_solicitados:
            print("\nSolicitud sin items.\n")
            return

        codigo = len(self.system.requisitions) + 5001
        solicitud = SolicitudInsumo(
            codigo, fecha_solicitud, responsable, items_solicitados
        )
        self.system.requisitions.append(solicitud)

        print("")
        print("=" * 64)
        print("SOLICITUD REGISTRADA CORRECTAMENTE")
        print(solicitud)
        print("=" * 64)

# =====================================================================
# GESTIONAR SOLICITUDES (RF 2.4)
# =====================================================================

    def obtener_solicitudes_pendientes(self):
        return [
            s
            for s in self.system.requisitions
            if s.estado == "pendiente"
        ]

    def verificar_disponibilidad_solicitud(self, solicitud):
        faltantes = []
        for item in solicitud.items:
            if item["cantidad"] > item["insumo"].stock_actual:
                faltantes.append(
                    (
                        item["insumo"],
                        item["cantidad"]
                        - item["insumo"].stock_actual,
                    )
                )
        return faltantes

    def gestionar_solicitudes_inventario(self):
        while True:
            pendientes = self.obtener_solicitudes_pendientes()

            if not pendientes:
                print("=" * 40)
                print("!NO HAY SOLICITUDES PENDIENTES¡")
                print("=" * 40)
                break

            print("=" * 40)
            print("SOLICITUDES PENDIENTES:")
            for s in pendientes:
                print(
                    f"{s.codigo} | {s.fecha_solicitud} | {s.responsable} | Items: {len(s.items)}"
                )
            print("=" * 40)

            try:
                codigo = int(
                    input("\nCódigo a Gestionar (0 para Regresar): ")
                )
            except ValueError:
                print("Código inválido.\n")
                continue

            if codigo == 0:
                break

            solicitud = next(
                (s for s in pendientes if s.codigo == codigo), None
            )

            if not solicitud:
                print("¡CODIGO DE SOLICITUD NO ENCONTRADO!\n")
                continue

            print(solicitud)

            faltantes = self.verificar_disponibilidad_solicitud(
                solicitud
            )

            if faltantes:
                print(
                    "\n!NO HAY STOCK SUFICIENTE PARA SER APROBADO¡\n"
                )
                for insumo, faltante in faltantes:
                    print(f"- {insumo.nombre}: faltan {faltante}")
            else:
                print("\n!STOCK SUFICIENTE PARA SER APROBADO¡")

            print("\nA = Aprobar | R = Rechazar | N = Nada")

            op = input("Opción: ").strip().lower()

            if op == "a":
                if faltantes:
                    print("\nNo se puede aprobar.\n")
                    continue

                for item in solicitud.items:
                    item["insumo"].stock_actual -= item["cantidad"]

                solicitud.estado = "aprobada"
                print("")
                print("=" * 40)
                print("!SOLICITUD APROBADA¡")
                print("=" * 40)
                print("")

            elif op == "r":
                solicitud.estado = "rechazada"
                print("")
                print("=" * 40)
                print("!SOLICITUD RECHAZADA¡")
                print("=" * 40)
                print("")

            elif op == "n":
                print("\nSin cambios.\n")
