# finance/reports.py

from .transactions import financial_records

def generate_report():
    print("\n--- Reporte Financiero ---")

    ingresos = sum(t["monto"] for t in financial_records if t["tipo"] == "ingreso")
    egresos = sum(t["monto"] for t in financial_records if t["tipo"] == "egreso")
    balance = ingresos - egresos

    print(f"Total Ingresos: ${ingresos}")
    print(f"Total Egresos:  ${egresos}")
    print(f"Balance Final:  ${balance}")
