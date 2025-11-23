# main.py

from customer.index import customer_menu
from inventory.index import inventory_menu
from sale.index import sale_menu
from user.index import user_menu
from finance.index import finance_menu


def main_menu():
    while True:
        print("\n=== POSINNOVATE PYTHON ===")
        print("1. Customer (Clientes)")
        print("2. Inventory (Inventario)")
        print("3. Sale (Ventas)")
        print("4. User (Usuarios)")
        print("5. Finance (Finanzas)")

        print("0. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            customer_menu()
        elif option == "2":
            inventory_menu()
        elif option == "3":
            sale_menu()
        elif option == "4":
            user_menu()
        elif option == "5":
            finance_menu()
        elif option == "0":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main_menu()
