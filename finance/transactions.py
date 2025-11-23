import json
import os
from datetime import datetime

# Ruta del archivo JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

# -------------------------------------------------------------
#  Asegurar que el archivo JSON existe
# -------------------------------------------------------------
def init_data_file():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump({"transactions": []}, f, indent=4)

# -------------------------------------------------------------
#  Cargar datos desde JSON
# -------------------------------------------------------------
def load_data():
    init_data_file()
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# -------------------------------------------------------------
#  Guardar datos en JSON
# -------------------------------------------------------------
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# -------------------------------------------------------------
#  Obtener el siguiente ID automático
# -------------------------------------------------------------
def get_next_id(transactions):
    if not transactions:
        return 1
    return max(t["id"] for t in transactions) + 1

# -------------------------------------------------------------
#  Registrar una nueva transacción (ingreso o egreso)
# -------------------------------------------------------------
def add_transaction(tipo, monto, descripcion):
    data = load_data()

    transactions = data["transactions"]

    nuevo_id = get_next_id(transactions)

    nueva_transaccion = {
        "id": nuevo_id,
        "tipo": tipo.lower(),  # ingreso / egreso
        "monto": float(monto),
        "descripcion": descripcion,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    transactions.append(nueva_transaccion)
    save_data(data)

    return nueva_transaccion

# -------------------------------------------------------------
#  Obtener todas las transacciones
# -------------------------------------------------------------
def get_all_transactions():
    data = load_data()
    return data["transactions"]

