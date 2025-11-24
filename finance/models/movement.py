from datetime import datetime


class FinancialMovement:
    def __init__(self, code, date, movement_type, concept, amount, reference=None):
        """
        movement_type: 'gasto' o 'ingreso'
        concept: texto corto (ej: 'Compra insumo super', 'Venta #7001')
        amount: valor positivo en pesos
        reference: puede ser un objeto Venta, Insumo, etc. (opcional)
        """
        self.code = code
        self.date = date or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.movement_type = movement_type
        self.concept = concept
        self.amount = amount
        self.reference = reference

    def __str__(self):
        tipo = "GASTO" if self.movement_type == "gasto" else "INGRESO"
        return (
            f"[{self.code}] {self.date} | {tipo:<7} | "
            f"${self.amount} | {self.concept}"
        )