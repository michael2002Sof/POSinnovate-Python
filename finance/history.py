from .transactions import get_all_transactions
import datetime

# -------------------------------------------------------------
#  Historial completo (ordenado por fecha)
# -------------------------------------------------------------
def show_history():
    transactions = get_all_transactions()

    if not transactions:
        print("\nNo hay historial financiero registrado.\n")
        return

    # Ordenar por fecha
    transactions.sort(key=lambda t: t["fecha"])

    print("\n=== HISTORIAL FINANCIERO ===")
    for t in transactions:
        print(f"""
ID:          {t['id']}
Tipo:        {t['tipo'].upper()}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

# -------------------------------------------------------------
#  Historial por tipo (ingresos / egresos)
# -------------------------------------------------------------
def history_by_type(tipo):
    tipo = tipo.lower()
    transactions = get_all_transactions()

    filtradas = [t for t in transactions if t["tipo"] == tipo]

    if not filtradas:
        print(f"\nNo hay transacciones de tipo {tipo}.\n")
        return

    print(f"\n=== HISTORIAL DE {tipo.upper()} ===")
    for t in filtradas:
        print(f"""
ID:          {t['id']}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

# -------------------------------------------------------------
#  Historial por fecha exacta
# -------------------------------------------------------------
def history_by_date(date_str):
    transactions = get_all_transactions()

    filtradas = [t for t in transactions if t["fecha"] == date_str]

    if not filtradas:
        print(f"\nNo hay transacciones registradas en la fecha {date_str}.\n")
        return

    print(f"\n=== HISTORIAL DEL {date_str} ===")
    for t in filtradas:
        print(f"""
ID:          {t['id']}
Tipo:        {t['tipo'].upper()}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

# -------------------------------------------------------------
#  Historial por rango de fechas
# -------------------------------------------------------------
def history_by_range(start_date, end_date):
    transactions = get_all_transactions()

    # Convertir a fecha real
    def parse(d):
        return datetime.datetime.strptime(d, "%Y-%m-%d")

    start = parse(start_date)
    end = parse(end_date)

    filtradas = [
        t for t in transactions 
        if start <= parse(t["fecha"]) <= end
    ]

    if not filtradas:
        print(f"\nNo hay transacciones entre {start_date} y {end_date}.\n")
        return

    print(f"\n=== HISTORIAL ENTRE {start_date} Y {end_date} ===")
    for t in filtradas:
        print(f"""
ID:          {t['id']}
Tipo:        {t['tipo'].upper()}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

