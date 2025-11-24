from datetime import datetime

from finance.models.movement import FinancialMovement


class FinanceController:
    def __init__(self, system):
        self.system = system

    # ===============================================================
    # RF 4.1 - Almacenar transacciones económicas
    # ===============================================================

    def registrar_gasto_insumo(self, insumo, monto, detalle_extra=""):
        """
        Registra un gasto asociado a un insumo (compra, reposición, etc.).
        Se puede llamar desde el controlador de insumos.
        """
        if monto <= 0:
            return

        code = len(self.system.financial_movements) + 9001
        date = datetime.now().strftime("%d/%m/%Y %H:%M")
        concept = f"Compra insumo '{insumo.nombre}' {detalle_extra}".strip()

        movimiento = FinancialMovement(
            code, date, "gasto", concept, monto, reference=insumo
        )
        self.system.financial_movements.append(movimiento)

    def registrar_ingreso_venta(self, venta):
        """
        Registra un ingreso asociado a una venta.
        Debe ser llamado desde el controlador de ventas al finalizar la venta.
        """
        if venta.total <= 0:
            return

        code = len(self.system.financial_movements) + 9001
        date = venta.date
        concept = f"Venta #{venta.code} al cliente {venta.customer_name}"

        movimiento = FinancialMovement(
            code, date, "ingreso", concept, venta.total, reference=venta
        )
        self.system.financial_movements.append(movimiento)

    # ===============================================================
    # RF 4.2 - Reporte detallado de gastos (insumos)
    # ===============================================================

    def reporte_gastos_insumos(self):
        gastos = [
            m for m in self.system.financial_movements
            if m.movement_type == "gasto"
        ]

        if not gastos:
            print("")
            print("=" * 60)
            print("NO HAY GASTOS REGISTRADOS (INSUMOS).")
            print("=" * 60)
            return

        print("")
        print("=" * 60)
        print("REPORTE DE GASTOS - INSUMOS")
        print("=" * 60)

        total = 0
        for m in gastos:
            print(m)
            total += m.amount

        print("-" * 60)
        print(f"TOTAL GASTOS EN INSUMOS: ${total}")
        print("=" * 60)

    # ===============================================================
    # RF 4.3 - Reporte de ingresos (productos vendidos)
    # ===============================================================

    def reporte_ingresos_ventas(self):
        ingresos = [
            m for m in self.system.financial_movements
            if m.movement_type == "ingreso"
        ]

        if not ingresos:
            print("")
            print("=" * 60)
            print("NO HAY INGRESOS REGISTRADOS (VENTAS).")
            print("=" * 60)
            return

        print("")
        print("=" * 60)
        print("REPORTE DE INGRESOS - VENTAS")
        print("=" * 60)

        total = 0
        for m in ingresos:
            print(m)
            total += m.amount

        print("-" * 60)
        print(f"TOTAL INGRESOS POR VENTAS: ${total}")
        print("=" * 60)

    # ===============================================================
    # RF 4.4 - Historial de compras (insumos) y ventas (productos)
    # ===============================================================

    def historial_movimientos(self):
        if not self.system.financial_movements:
            print("")
            print("=" * 60)
            print("NO HAY MOVIMIENTOS FINANCIEROS REGISTRADOS.")
            print("=" * 60)
            return

        print("")
        print("=" * 60)
        print("HISTORIAL DE MOVIMIENTOS FINANCIEROS")
        print("=" * 60)

        for m in self.system.financial_movements:
            print(m)

        print("=" * 60)