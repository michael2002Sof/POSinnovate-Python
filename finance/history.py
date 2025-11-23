# finance/history.py

from .transactions import financial_records

def show_history():
    print("\n--- Historial de Transacciones ---")

    if not financial_records:
        print("No hay movimientos registrados.")
        return

    for i, t in enumerate(financial_records, start=1):
        print(f"\nMovimiento {i}:")
        print(f" - Tipo: {t['tipo']}")
        print(f" - Monto: {t['monto']}")
        print(f" - Método: {t['metodo']}")
        print(f" - Descripción: {t['descripcion']}")
