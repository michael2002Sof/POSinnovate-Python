# finance/index.py

from .transactions import register_transaction
from .reports import generate_report
from .history import show_history

def finance_menu():
    while True:
        print("\n=== MÓDULO DE FINANZAS ===")
        print("1. Registrar transacción")
        print("2. Generar reporte")
        print("3. Ver historial")
        print("0. Volver al menú principal")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_transaction()
        elif option == "2":
            generate_report()
        elif option == "3":
            show_history()
        elif option == "0":
            break
        else:
            print("Opción inválida, intente otra vez.")
