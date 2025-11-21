from datetime import datetime
from inventory.modules.product import productos
from .voucher import generar_voucher


# ===============================================================
# HISTORIAL GLOBAL DE VENTAS
# ===============================================================

historial_ventas = []


# ===============================================================
# REGISTRO DE VENTAS (RF 3.1 + RF 3.2)
# ===============================================================

def registrar_venta():
    print("\n====================================================")
    print("              REGISTRO DE VENTA (RF 3.1)")
    print("====================================================")



    if not productos:
        print("\nNO HAY PRODUCTOS REGISTRADOS EN INVENTARIO.\n")
        return

    carrito = []
    cantidades = []
    total = 0

    cliente = input("Nombre del cliente: ").strip()


    # -------------------------------
    # SELECCIÓN DE PRODUCTOS
    # -------------------------------
    while True:
        print("\n----- PRODUCTOS DISPONIBLES -----")
        for p in productos:
            print(f"{p.codigo} - {p.marca} {p.modelo} | Talla {p.talla} | ${p.precio_venta} | Stock: {p.cantidad}")

        try:
            codigo = int(input("\nDigite el código del producto: "))
        except ValueError:
            print("Código inválido.\n")
            continue

        encontrado = next((p for p in productos if p.codigo == codigo), None)

        if not encontrado:
            print("Producto no encontrado.\n")
            continue

        # Cantidad
        try:
            cant = int(input("Cantidad a comprar: "))
        except:
            print("Cantidad inválida.\n")
            continue

        if cant <= 0 or cant > encontrado.cantidad:
            print("Cantidad no disponible.\n")
            continue

        carrito.append(encontrado)
        cantidades.append(cant)
        total += encontrado.precio_venta * cant

        otro = input("¿Agregar otro producto? (SI/NO): ").strip().lower()
        if otro != "si":
            break

    # -------------------------------
    # REGISTRAR FECHA
    # -------------------------------
    fecha = datetime.now().strftime("%d/%m/%Y")

    # -------------------------------
    # GENERAR VOUCHER (RF 3.2)
    # -------------------------------
    voucher_id = generar_voucher(cliente, carrito, cantidades, fecha, total)

    # -------------------------------
    # GUARDAR EN HISTORIAL
    # -------------------------------
    historial_ventas.append({
        "cliente": cliente,
        "productos": [f"{p.marca} {p.modelo}" for p in carrito],
        "cantidad_total": sum(cantidades),
        "total": total,
        "fecha": fecha,
        "estado": "en proceso",
        "voucher_id": voucher_id
    })

    # -------------------------------
    # CONFIRMACIÓN
    # -------------------------------
    print("\n====================================================")
    print("           ¡VENTA REGISTRADA CON ÉXITO!")
    print("====================================================")
    print(f"Total: ${total}")
    print(f"Voucher generado: {voucher_id}")
    print("====================================================\n")
