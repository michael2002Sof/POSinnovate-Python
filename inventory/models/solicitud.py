class SolicitudInsumo:
    def __init__(self, codigo, fecha_solicitud, responsable, items, estado="pendiente"):
        self.codigo = codigo
        self.fecha_solicitud = fecha_solicitud
        self.responsable = responsable
        self.estado = estado
        self.items = items 

    def __str__(self):
        txt = [
            "================================================================",
            f"Solicitud {self.codigo} - Fecha: {self.fecha_solicitud}",
            f"Responsable: {self.responsable} | Estado: {self.estado}",
            "Items solicitados:\n",
        ]

        for item in self.items:
            insumo = item["insumo"]
            cantidad = item["cantidad"]
            txt.append(
                f"- {insumo.nombre} | Código: {insumo.codigo} - Cantidad Solicitada: {cantidad} {insumo.unidad_medida}"
            )

        txt.append("================================================================")
        return "\n".join(txt)
