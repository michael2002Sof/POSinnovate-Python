from .insumo import insumos
from datetime import datetime

productos = []

# ============================================================================================
# CLASE PRODUCTO
# ============================================================================================

class Producto:
    def __init__(self, fecha_registro, marca, modelo, tipo, talla, color, cantidad, precio_venta):
        self.codigo = len(productos) + 3001
        self.fecha_registro = fecha_registro
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.talla = talla
        self.color = color
        self.cantidad = cantidad
        self.precio_venta = precio_venta

        if 36 <= self.talla <= 39:
            self.genero = "dama"
        elif 40 <= self.talla <= 45:
            self.genero = "caballero"
        else:
            self.genero = "no definido"

        self.estado = "disponible" if self.cantidad > 0 else "agotado"

    def __str__(self):
        return (
            f"\n================================================================\n"
            f"Fecha registro: {self.fecha_registro}\n"
            f"Código: {self.codigo}\n"
            f"Marca: {self.marca} | Modelo: {self.modelo} | Tipo: {self.tipo}\n"
            f"Talla: {self.talla} | Color: {self.color} | Género: {self.genero}\n"
            f"Cantidad: {self.cantidad} par(es)\n"
            f"Precio unitario: ${self.precio_venta}\n"
            f"Estado: {self.estado}\n"
            f"================================================================"
        )

# ===============================================================
# REGISTRAR PRODUCTOS (RF 5.2)
# ===============================================================

    def registrar_productos():
        tipos_validos = ["deportivo", "casual", "formal", "sandalia", "bota"]

        while True:
            # Fecha automática con datetime (sin pedir por teclado)
            fecha_registro_ = datetime.now().strftime("%d/%m/%Y")
            print(f"\nFecha de Registro: {fecha_registro_}")

            marca_ = input("Marca: ").strip().lower()
            modelo_ = input("Modelo: ").strip().lower()

            while True:
                tipo_ = input(f"Tipo ({', '.join(tipos_validos)}): ").strip().lower()
                if tipo_ in tipos_validos:
                    break
                print("Tipo inválido, ingresa un tipo de modelo permitido.\n")

            # Talla 36 a 45
            while True:
                try:
                    talla_ = float(input("Talla (36-45): "))
                    if 36 <= talla_ <= 45:
                        break
                    else:
                        print("Talla inválida, ingresa un número entre 36 y 45.\n")
                except ValueError:
                    print("Talla inválida, ingresa un número válido.\n")

            color_ = input("Color: ").strip().lower()

# ===================================================================
# SI EXISTE - MODIFICAR
# ===================================================================

            existente = next((p for p in productos if 
                              p.marca == marca_ and p.modelo == modelo_ and 
                              p.tipo == tipo_ and p.talla == talla_ and p.color == color_), None)

            if existente:
                print("=" * 40) 
                print("ADVERTENCIA:")
                print("\nProducto ya registrado.")
                print("=" * 40)

                while True:
                    op = input("\n¿Desea actualizar cantidad y precio? (SI/NO): ").strip().lower()
                    
                    if op == "si":

                        while True:
                            try:
                                extra = int(input("Cantidad a agregar: "))
                                if extra >= 0:
                                    break
                                else:
                                    print("La cantidad debe ser 0 o mayor.\n")
                            except ValueError:
                                print("Cantidad inválida.\n")

                        while True:
                            precio_ = input("Nuevo precio (o enter para mantener): ").strip()

                            if precio_ == "":
                                nuevo_precio = existente.precio_venta
                                break

                            try:
                                nuevo_precio = float(precio_)
                                if nuevo_precio >= 0:
                                    break
                                else:
                                    print("El precio debe ser igual o mayor a 0.\n")
                            except ValueError:
                                print("Precio inválido.\n")

                        existente.cantidad += extra
                        existente.precio_venta = nuevo_precio
                        existente.estado = "disponible" if existente.cantidad > 0 else "agotado"

                        print("")
                        print("=" * 40) 
                        print("¡PRODUCTO ACTUALIZADO CORRECTAMENTE!")
                        print("=" * 40) 
                        print("")
                        break

                    elif op == "no":
                        print("¡NO SE MODIFICO EL PRODUCTO!.\n")
                        break

                    else:
                        print("Opción inválida. Responda SI o NO.\n")


                cont = input("¿Registrar otro? (SI/NO): ").strip().lower()
                if cont != "si": break
                continue

# ===================================================================
# NO EXISTE - REGISTRAR NUEVO
# ===================================================================

            while True:
                try:
                    cantidad_ = int(input("Cantidad: "))
                    if cantidad_ > 0:
                        break
                    else:
                        print("La cantidad debe ser mayor a 0.\n")
                except ValueError:
                    print("Cantidad inválida, ingresa un número entero.\n")

            while True:
                try:
                    precio_venta_ = float(input("Precio venta: "))
                    if precio_venta_ > 0:
                        break
                    else:
                        print("El precio debe ser mayor a 0.\n")
                except ValueError:
                    print("Precio inválido, ingresa un número válido.\n")


            producto = Producto(fecha_registro_, marca_, modelo_, tipo_, talla_, color_, cantidad_, precio_venta_)
            productos.append(producto)

            print("\nProducto registrado.\n")

            cont = input("¿Registrar otro? (SI/NO): ").strip().lower()
            if cont != "si":
                break

# ===============================================================
# CONSULTA DE INSUMOS DESDE PRODUCCIÓN (RF 5.1)
# ===============================================================

def consultar_insumos_produccion():
    if not insumos:
        print("")
        print("=" * 40)
        print("¡NO HAY INSUMOS REGISTRADOS!")
        print("=" * 40)
        return

    while True:
        print("")
        print("=" * 40)
        print("CONSULTA DE INSUMOS")
        print("=" * 40)
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Ver todos")
        print("4. Volver")
        print("=" * 40)
        print("")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                c = int(input("Código: "))
            except ValueError:
                print("Código inválido.")
                continue

            encontrado = next((i for i in insumos if i.codigo == c), None)

            print(encontrado if encontrado else "No encontrado.\n")

        elif opcion == "2":
            n = input("Nombre: ").strip().lower()
            encontrados = [i for i in insumos if n in i.nombre]

            if encontrados:
                for i in encontrados:
                    print(i)
            else:
                print("No encontrados.\n")

        elif opcion == "3":
            for i in insumos:
                print(i)

        elif opcion == "4":
            break

        else:
            print("Opción inválida.\n")
