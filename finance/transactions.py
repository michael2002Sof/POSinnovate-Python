# finance/transactions.py

financial_records = []

def register_transaction():
    print("\n--- Registrar Transacción ---")

    tipo = input("Tipo (ingreso/egreso): ").lower()
    if tipo not in ["ingreso", "egreso"]:
        print("Tipo inválido.")
        return
    
    monto = float(input("Monto: "))
    metodo = input("Método de pago: ")
    descripcion = input("Descripción: ")

    trans = {
        "tipo": tipo,
        "monto": monto,
        "metodo": metodo,
        "descripcion": descripcion
    }

    financial_records.append(trans)

    print("✔ Transacción registrada con éxito.")
