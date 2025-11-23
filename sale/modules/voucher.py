# sale/modules/voucher.py

from datetime import datetime


class VoucherManager:
    def __init__(self):
        self.historial_vouchers = []

    def generar_voucher(self, cliente, carrito, cantidades, fecha, total):
        voucher_id = f"VCH-{len(self.historial_vouchers)+1:05d}"

        contenido = [
            "\n==============================================",
            "               VOUCHER DE VENTA               ",
            "==============================================",
            f"Fecha: {fecha}",
            f"Código: {voucher_id}",
            "----------------------------------------------",
            f"Cliente: {cliente}",
            "----------------------------------------------",
            "Productos:",
        ]

        for p, cant in zip(carrito, cantidades):
            subtotal = cant * p.precio_venta
            contenido.append(
                f"  - {p.marca} {p.modelo} | {cant} und | "
                f"${p.precio_venta} c/u | Subtotal: ${subtotal}"
            )

        contenido.append("----------------------------------------------")
        contenido.append(f"TOTAL A PAGAR: ${total}")
        contenido.append("==============================================")
        contenido.append("Gracias por su compra.")
        contenido.append("==============================================\n")

        voucher_text = "\n".join(contenido)

        # Guardamos
        self.historial_vouchers.append({
            "voucher_id": voucher_id,
            "cliente": cliente,
            "fecha": fecha,
            "total": total,
            "voucher_text": voucher_text,
            "estado": "en proceso"
        })

        print(voucher_text)
        return voucher_id
