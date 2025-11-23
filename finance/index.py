from .transactions import add_transaction, show_transactions
from .history import (
    show_history,
    history_by_type,
    history_by_date,
    history_by_range
)

# ============================================================
#                      MENÚ FINANZAS
# ============================================================
def finance_menu():
    while True:
        print("\n===== MÓDULO FINANZAS =====")
        print("1. Registrar transacción (Ingreso/Egreso)")
        print("2. Ver todas las transacciones")
        print("3. Historial completo")
        print("4. Historial por tipo (Ingresos/Egresos)")
        print("5. Historial por fecha exacta")
        print("6. Historial por rango de fechas")
        print("0. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        # ------------------------------------------
        # 1. Registrar transacción
        # ------------------------------------------
        if opcion == "1":
            tipo = input("Tipo (ingreso/egreso): ").lower()
            monto = float(input("Monto: "))
            descripcion = input("Descripción: ")

            add_transaction(tipo, monto, descripcion)
            print("\nTransacción registrada correctamente.\n")

        # ------------------------------------------
        # 2. Ver todas las transacciones
        # ------------------------------------------
        elif opcion == "2":
            show_transactions()

        # ------------------------------------------
        # 3. Historial completo
        # ------------------------------------------
        elif opcion == "3":
            show_history()

        # ------------------------------------------
        # 4. Historial por tipo
        # ------------------------------------------
        elif opcion == "4":
            tipo = input("Ingrese tipo (ingreso/egreso): ").lower()
            history_by_type(tipo)

        # ------------------------------------------
        # 5. Historial por fecha
        # ------------------------------------------
        elif opcion == "5":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            history_by_date(fecha)

        # ------------------------------------------
        # 6. Historial por rango
        # ------------------------------------------
        elif opcion == "6":
            inicio = input("Fecha de inicio (YYYY-MM-DD): ")
            fin = input("Fecha final (YYYY-MM-DD): ")
            history_by_range(inicio, fin)

        # ------------------------------------------
        # 0. Salir
        # ------------------------------------------
        elif opcion == "0":
            print("\nRegresando al menú principal...\n")
            break

        else:
            print("Opción no válida. Intente de nuevo.")
