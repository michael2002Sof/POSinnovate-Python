import json
import os
from datetime import datetime
from typing import List, Dict, Any


class TransactionRepository:

    def __init__(self):
        # Ruta del archivo JSON
        self.DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")
        self._ensure_data_file()

    # -------------------------------------------------------------
    #  Asegurar que el archivo JSON existe
    # -------------------------------------------------------------
    def _ensure_data_file(self):
        if not os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, "w", encoding="utf-8") as f:
                json.dump({"transactions": []}, f, indent=4)

    # -------------------------------------------------------------
    #  Cargar datos desde JSON
    # -------------------------------------------------------------
    def _load_data(self) -> Dict[str, Any]:
        self._ensure_data_file()
        with open(self.DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    # -------------------------------------------------------------
    #  Guardar datos en JSON
    # -------------------------------------------------------------
    def _save_data(self, data: Dict[str, Any]):
        with open(self.DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    # -------------------------------------------------------------
    #  Obtener el siguiente ID automático
    # -------------------------------------------------------------
    def _get_next_id(self, transactions: List[Dict[str, Any]]) -> int:
        return max((t["id"] for t in transactions), default=0) + 1

    # -------------------------------------------------------------
    #  Registrar una nueva transacción (ingreso o egreso)
    # -------------------------------------------------------------
    def add_transaction(self, tipo: str, monto: float, descripcion: str) -> Dict[str, Any]:
        data = self._load_data()
        transactions = data["transactions"]

        nuevo_id = self._get_next_id(transactions)

        nueva_transaccion = {
            "id": nuevo_id,
            "tipo": tipo.lower(),
            "monto": float(monto),
            "descripcion": descripcion,
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        transactions.append(nueva_transaccion)
        self._save_data(data)

        return nueva_transaccion

    # -------------------------------------------------------------
    #  Obtener todas las transacciones
    # -------------------------------------------------------------
    def get_all_transactions(self) -> List[Dict[str, Any]]:
        data = self._load_data()
        return data["transactions"]
