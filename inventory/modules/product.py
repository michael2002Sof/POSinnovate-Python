from .insumo import insumos

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

# ===============================================================
# REGISTRAR PRODUCTOS (RF 5.2)
# ===============================================================

    def registrar_productos():
        tipos_validos = ["deportivo", "casual", "formal", "sandalia", "bota"]

        while True:
            # Validar fecha
            while True:
                fecha_registro_ = input("Fecha (DD/MM/AAAA): ").strip()
                p = fecha_registro_.split("/")
                if len(p) == 3 and all(x.isdigit() for x in p):
                    d, m, a = map(int, p)
                    if 1 <= d <= 31 and 1 <= m <= 12 and a >= 2025:
                        break
                print("Fecha inválida.\n")

            marca_ = input("Marca: ").strip().lower()
            modelo_ = input("Modelo: ").strip().lower()

            while True:
                tipo_ = input(f"Tipo ({', '.join(tipos_validos)}): ").strip().lower()
                if tipo_ in tipos_validos:
                    break
                print("Tipo inválido.\n")

            # Talla 36 a 45
            while True:
                try:
                    talla_ = float(input("Talla (36-45): "))
                    if 36 <= talla_ <= 45:
                        break
                except:
                    pass
                print("Talla inválida.\n")

            color_ = input("Color: ").strip().lower()

            # Buscar si existe
            existente = next((p for p in productos if 
                              p.marca == marca_ and p.modelo == modelo_ and 
                              p.tipo == tipo_ and p.talla == talla_ and p.color == color_), None)

            if existente:
                print("\nProducto ya registrado.")

                while True:
                    op = input("¿Actualizar cantidad y precio? (SI/NO): ").strip().lower()
                    if op == "si":
                        while True:
                            try:
                                extra = int(input("Cantidad a agregar: "))
                                if extra >= 0: break
                            except: pass
                            print("Cantidad inválida.\n")

                        while True:
                            precio_ = input("Nuevo precio (o enter para mantener): ").strip()
                            if precio_ == "":
                                nuevo_precio = existente.precio_venta
                                break
                            try:
                                nuevo_precio = float(precio_)
                                if nuevo_precio >= 0: break
                            except: pass
                            print("Precio inválido.\n")

                        existente.cantidad += extra
                        existente.precio_venta = nuevo_precio
                        existente.estado = "disponible" if existente.cantidad > 0 else "agotado"

                        print("\nProducto actualizado.\n")
                        break

                    elif op == "no":
                        print("\nNo se modificó.\n")
                        break

                cont = input("¿Registrar otro? (SI/NO): ").strip().lower()
                if cont != "si": break
                continue

            # Si no existe; registrar uno nuevo
            while True:
                try:
                    cantidad_ = int(input("Cantidad: "))
                    if cantidad_ >= 0: break
                except: pass
                print("Cantidad inválida.\n")

            while True:
                try:
                    precio_venta_ = float(input("Precio venta: "))
                    if precio_venta_ >= 0: break
                except: pass
                print("Precio inválido.\n")

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
        print("\nInventario vacío.\n")
        return

    while True:
        print("\nConsulta de insumos desde producción")
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Ver todos")
        print("4. Volver")

        opcion = input("Opción: ").strip()

        if opcion == "1":
            try:
                c = int(input("Código: "))
            except:
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
