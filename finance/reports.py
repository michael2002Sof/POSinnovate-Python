from .transactions import get_all_transactions

# -------------------------------------------------------------
#  Mostrar TODAS las transacciones
# -------------------------------------------------------------
def show_all_transactions():
    transactions = get_all_transactions()

    if not transactions:
        print("\nNo hay transacciones registradas.\n")
        return

    print("\n=== TODAS LAS TRANSACCIONES ===")
    for t in transactions:
        print(f"""
ID:          {t['id']}
Tipo:        {t['tipo'].upper()}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

# -------------------------------------------------------------
#  Filtrar transacciones por tipo (ingreso / egreso)
# -------------------------------------------------------------
def filter_by_type(tipo):
    transactions = get_all_transactions()
    tipo = tipo.lower()

    filtradas = [t for t in transactions if t["tipo"] == tipo]

    if not filtradas:
        print(f"\nNo se encontraron transacciones del tipo: {tipo}\n")
        return

    print(f"\n=== TRANSACCIONES DE TIPO {tipo.upper()} ===")
    for t in filtradas:
        print(f"""
ID:          {t['id']}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")

# -------------------------------------------------------------
#  Buscar transacción por ID
# -------------------------------------------------------------
def search_by_id(transaction_id):
    transactions = get_all_transactions()

    for t in transactions:
        if t["id"] == transaction_id:
            print("\n=== TRANSACCIÓN ENCONTRADA ===")
            print(f"""
ID:          {t['id']}
Tipo:        {t['tipo'].upper()}
Monto:       ${t['monto']}
Descripción: {t['descripcion']}
Fecha:       {t['fecha']}
-----------------------------""")
            return

    print("\nNo existe una transacción con ese ID.\n")

# -------------------------------------------------------------
#  Mostrar resumen financiero (ingresos, egresos y total)
# -------------------------------------------------------------
def financial_summary():
    transactions = get_all_transactions()

    ingresos = sum(t["monto"] for t in transactions if t["tipo"] == "ingreso")
    egresos  = sum(t["monto"] for t in transactions if t["tipo"] == "egreso")

    total = ingresos - egresos

    print("\n=== RESUMEN FINANCIERO ===")
    print(f"Ingresos:  ${ingresos}")
    print(f"Egresos:   ${egresos}")
    print(f"Balance:   ${total}")
    print("-----------------------------\n")

