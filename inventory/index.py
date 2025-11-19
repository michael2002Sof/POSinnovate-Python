from .modules.insumo import menu_inventario
from .modules.product import menu_produccion

def menu_principal():
    while True:
        print("")
        print("=" * 50)
        print("POSInnovate - Módulo Inventory")
        print("=" * 50)
        print("1. Ingresar como Gestor de Inventario")
        print("2. Ingresar como Gestor de Producción")
        print("3. Salir\n")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            menu_inventario()

        elif opcion == "2":
            menu_produccion()

        elif opcion == "3":
            print("\nSaliendo del sistema Inventory...\n")
            break

        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu_principal()
