# ================================================================================================
# Módulo: voucher.py  (RF 3.2 – Generar voucher digital)
# ================================================================================================

import datetime

# Lista global donde se almacenan todos los vouchers generados
historial_vouchers = []


def generar_voucher(venta):
    """
    Recibe un objeto 'venta' (generado en RF 3.1) y construye el voucher
    en formato de texto, listo para imprimirse en pantalla o guardarse.
    """

    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    contenido = []
    contenido.append("\n==============================================")
    contenido.append("               VOUCHER DE VENTA               ")
    contenido.append("==============================================")
    contenido.append(f"Fecha: {fecha_actual}")
    contenido.append(f"Código de Venta: {venta.codigo}")
    contenido.append("----------------------------------------------")
    contenido.append("Cliente:")
    contenido.append(f"  Nombre: {venta.cliente_nombre}")
    contenido.append(f"  Identificación: {venta.cliente_id}")
    contenido.append("----------------------------------------------")
    contenido.append("Productos:")

    total_general = 0

    for item in venta.items:
        producto = item["producto"]
        cantidad = item["cantidad"]
        precio_unit = item["precio_unit"]
        subtotal = cantidad * precio_unit
        total_general += subtotal

        contenido.append(
            f"  - {producto.nombre} | {cantidad} und | "
            f"${precio_unit:,.0f} c/u | Subtotal: ${subtotal:,.0f}"
        )

    contenido.append("----------------------------------------------")
    contenido.append(f"TOTAL A PAGAR: ${total_general:,.0f}")
    contenido.append("==============================================")
    contenido.append("Gracias por su compra.")
    contenido.append("==============================================\n")

    # Convertir lista a texto final
    voucher_texto = "\n".join(contenido)

    # Guardar en historial para RF 3.3 (seguimiento)
    historial_vouchers.append({
        "codigo": venta.codigo,
        "cliente": venta.cliente_nombre,
        "fecha": fecha_actual,
        "voucher": voucher_texto,
        "estado": venta.estado
    })

    return voucher_texto
    
