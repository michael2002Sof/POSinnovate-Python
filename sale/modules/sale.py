# sale/modules/sale.py

from inventory.modules.product import products   # ← IMPORTACIÓN CLAVE

sales_history = []

def register_sale():
    print("\n--- Registrar Venta ---")

    if not products:
        print("No hay productos disponibles en inventario para vender.")
        return

    print("\nProductos disponibles:")
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['nombre']} - ${p['precio_venta']} - Stock: {p['stock']}")

    try:
        option = int(input("\nSeleccione el producto: "))
        producto = products[option - 1]
    except:
        print("Opción inválida.")
        return

    cantidad = int(input("Ingrese cantidad a vender: "))

    if cantidad > producto["stock"]:
        print("No hay suficiente stock.")
        return

    total = cantidad * producto["precio_venta"]

    # Reducir stock
    producto["stock"] -= cantidad

    # Registrar venta
    venta = {
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "precio_unit": producto["precio_venta"],
        "total": total
    }

    sales_history.append(venta)

    print("\nVenta registrada con éxito.")
    print(f"Producto: {venta['producto']}")
    print(f"Cantidad: {venta['cantidad']}")
    print(f"Total: ${venta['total']}")

def sale_menu():
    while True:
        print("\n--- Módulo de Ventas ---")
        print("1. Registrar Venta")
        print("2. Ver Historial de Ventas")
        print("0. Volver")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_sale()
        elif option == "2":
            print("\nHistorial de ventas:")
            for v in sales_history:
                print(v)
        elif option == "0":
            break
        else:
            print("Opción no válida.")
# sale/modules/sale.py

from inventory.modules.product import products   # ← IMPORTACIÓN CLAVE

sales_history = []

def register_sale():
    print("\n--- Registrar Venta ---")

    if not products:
        print("No hay productos disponibles en inventario para vender.")
        return

    print("\nProductos disponibles:")
    for i, p in enumerate(products, start=1):
        print(f"{i}. {p['nombre']} - ${p['precio_venta']} - Stock: {p['stock']}")

    try:
        option = int(input("\nSeleccione el producto: "))
        producto = products[option - 1]
    except:
        print("Opción inválida.")
        return

    cantidad = int(input("Ingrese cantidad a vender: "))

    if cantidad > producto["stock"]:
        print("No hay suficiente stock.")
        return

    total = cantidad * producto["precio_venta"]

    # Reducir stock
    producto["stock"] -= cantidad

    # Registrar venta
    venta = {
        "producto": producto["nombre"],
        "cantidad": cantidad,
        "precio_unit": producto["precio_venta"],
        "total": total
    }

    sales_history.append(venta)

    print("\nVenta registrada con éxito.")
    print(f"Producto: {venta['producto']}")
    print(f"Cantidad: {venta['cantidad']}")
    print(f"Total: ${venta['total']}")

def sale_menu():
    while True:
        print("\n--- Módulo de Ventas ---")
        print("1. Registrar Venta")
        print("2. Ver Historial de Ventas")
        print("0. Volver")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_sale()
        elif option == "2":
            print("\nHistorial de ventas:")
            for v in sales_history:
                print(v)
        elif option == "0":
            break
        else:
            print("Opción no válida.")
