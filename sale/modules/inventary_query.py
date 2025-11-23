# sale/modules/inventary_query.py

from inventory.modules.product import productos


class InventarioManager:
    def consultar_disponibilidad(self):
        if not productos:
            print("\n==============================================")
            print("   ¡NO HAY PRODUCTOS REGISTRADOS!")
            print("==============================================\n")
            return

        while True:
            print("\n==============================================")
            print("      CONSULTA DE DISPONIBILIDAD (RF 3.4)")
            print("==============================================")
            print("1. Buscar por modelo")
            print("2. Buscar por marca")
            print("3. Buscar por categoría")
            print("4. Ver inventario completo")
            print("5. Volver")
            print("==============================================")

            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                modelo = input("Modelo: ").lower()
                self._mostrar([p for p in productos if modelo in p.modelo.lower()])

            elif opcion == "2":
                marca = input("Marca: ").lower()
                self._mostrar([p for p in productos if p.marca.lower() == marca])

            elif opcion == "3":
                tipo = input("Categoría: ").lower()
                self._mostrar([p for p in productos if p.tipo.lower() == tipo])

            elif opcion == "4":
                self._mostrar(productos)

            elif opcion == "5":
                break

    def _mostrar(self, lista):
        if not lista:
            print("\nNo se encontraron productos.\n")
            return

        print("\n================== RESULTADOS ==================\n")
        for p in lista:
            print(f"Código: {p.codigo}")
            print(f"Marca: {p.marca}")
            print(f"Modelo: {p.modelo}")
            print(f"Tipo: {p.tipo}")
            print(f"Talla: {p.talla}")
            print(f"Color: {p.color}")
            print(f"Cantidad: {p.cantidad}")
            print(f"Precio: ${p.precio_venta}")
            print("----------------------------------")
