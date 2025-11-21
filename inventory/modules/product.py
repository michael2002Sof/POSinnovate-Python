from .insumo import insumos
from .solicitud import solicitar_insumos

#=================================================================================================
# Clase de Productos
#=================================================================================================

productos = []

class Producto:
    def __init__(self,
                 fecha_registro,
                 marca,
                 modelo,
                 tipo,
                 talla,
                 color,
                 cantidad,
                 precio_venta):

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

#=================================================================================================
# Registro de Productos (RF 5.2)
#=================================================================================================

    def registrar_productos():
        tipos_validos = ["deportivo", "casual", "formal", "sandalia", "bota"]

        while True:
            # Fecha de registro con validación
            while True:
                fecha_registro_ = input("Ingrese la fecha de registro (DD/MM/AAAA): ").strip()
                partes = fecha_registro_.split("/")

                if len(partes) == 3:
                    dia, mes, año = partes

                    if dia.isdigit() and mes.isdigit() and año.isdigit():
                        if len(dia) == 2 and len(mes) == 2 and len(año) == 4:
                            dia = int(dia)
                            mes = int(mes)
                            año = int(año)

                            if 1 <= dia <= 31 and 1 <= mes <= 12 and año >= 2025:
                                break

                print("Fecha inválida. Debe estar en formato DD/MM/AAAA.\n")

            marca_ = input("Ingresa la marca del zapato: ").strip().lower()
            modelo_ = input("Ingresa el modelo del zapato: ").strip().lower()

            while True:
                print("Tipos válidos:", ", ".join(tipos_validos))
                tipo_ = input("Ingresa el tipo de zapato: ").strip().lower()
                if tipo_ in tipos_validos:
                    break
                else:
                    print("Tipo no válido, intentelo nuevamente.\n")

            # Validación estricta de talla (36–45)
            while True:
                talla_texto = input("Ingresa la talla del zapato (36 a 45): ").strip()
                try:
                    talla_ = float(talla_texto)
                    if 36 <= talla_ <= 45:
                        break
                    else:
                        print("Talla fuera de rango. Solo se aceptan tallas entre 36 y 45.\n")
                except ValueError:
                    print("Talla inválida. Debe ser un número.\n")

            color_ = input("Ingresa el color del zapato: ").strip().lower()

            # Buscar si ya existe un producto con misma marca, modelo, tipo, talla y color
            producto_existente = None
            for producto in productos:
                if (producto.marca == marca_ and
                    producto.modelo == modelo_ and
                    producto.tipo == tipo_ and
                    producto.talla == talla_ and
                    producto.color == color_):
                    producto_existente = producto
                    break

            if producto_existente is not None:
                print("\nEste producto ya se encuentra registrado con las mismas características.")
                while True:
                    opcion_2 = input("¿Desea actualizar solo la cantidad y el precio unitario? (SI/NO): ").strip().lower()
                    if opcion_2 == "si":
                        # Cantidad a sumar
                        while True:
                            cantidad_texto = input("Ingresa la cantidad de pares a agregar: ").strip()
                            try:
                                cantidad_extra = int(cantidad_texto)
                                if cantidad_extra >= 0:
                                    break
                                else:
                                    print("Cantidad negativa no permitida.\n")
                            except ValueError:
                                print("Cantidad inválida.\n")

                        # Nuevo precio unitario (reemplaza el anterior)
                        while True:
                            precio_texto = input("Ingresa el nuevo precio de venta por par (o deja vacío para mantener el actual): ").strip()
                            if precio_texto == "":
                                nuevo_precio = producto_existente.precio_venta
                                break
                            try:
                                nuevo_precio = float(precio_texto)
                                if nuevo_precio >= 0:
                                    break
                                else:
                                    print("El precio no puede ser negativo.\n")
                            except ValueError:
                                print("Precio inválido.\n")

                        # Actualizar producto existente
                        producto_existente.cantidad += cantidad_extra
                        producto_existente.precio_venta = nuevo_precio
                        producto_existente.estado = "disponible" if producto_existente.cantidad > 0 else "agotado"

                        print("\nProducto actualizado correctamente.")
                        print(f"Nueva cantidad: {producto_existente.cantidad} pares")
                        print(f"Nuevo precio unitario: ${producto_existente.precio_venta}\n")
                        break

                    elif opcion_2 == "no":
                        print("No se modificó el producto.\n")
                        break
                    else:
                        print("Opción inválida, responde SI o NO.\n")

                continuar = input("¿Deseas registrar otro producto? (SI/NO): ").strip().lower()
                if continuar != "si":
                    print("\nRegistro de productos finalizado.\n")
                    break
                else:
                    continue

            # Si no existe producto igual, se registra como nuevo
            while True:
                cantidad_texto = input("Ingresa la cantidad de pares producidos: ").strip()
                try:
                    cantidad_ = int(cantidad_texto)
                    if cantidad_ >= 0:
                        break
                    else:
                        print("Cantidad negativa no permitida.\n")
                except ValueError:
                    print("Cantidad inválida.\n")

            while True:
                precio_texto = input("Ingresa el precio de venta por par: ").strip()
                try:
                    precio_venta_ = float(precio_texto)
                    if precio_venta_ >= 0:
                        break
                    else:
                        print("El precio no puede ser negativo.\n")
                except ValueError:
                    print("Precio inválido.\n")

            producto = Producto(
                fecha_registro_,
                marca_,
                modelo_,
                tipo_,
                talla_,
                color_,
                cantidad_,
                precio_venta_
            )

            productos.append(producto)
            print("Producto registrado correctamente.\n")

            # Preguntar si desea registrar otro
            continuar = input("¿Deseas registrar otro producto? (SI/NO): ").strip().lower()
            if continuar != "si":
                print("\nRegistro de productos finalizado.\n")
                break

    def __str__(self):
        return (
            f"Fecha: {self.fecha_registro}:\n"
            f"Codigo: {self.codigo} | Marca: {self.marca} | Género: {self.genero}.\n"
            f"Modelo: {self.modelo} - Tipo: {self.tipo} - Talla: {self.talla}.\n"
            f"Color: {self.color} - Cantidad: {self.cantidad} pares - "
            f"Precio: ${self.precio_venta} - Estado: {self.estado}."
        )

#=================================================================================================
# Consultar insumos registrados en inventario (RF 5.1)
#=================================================================================================

def consultar_insumos_produccion():
    if not insumos:
        print("=" * 40)
        print("\nNo hay insumos registrados en inventario.\n")
        print("=" * 40)
        return

    while True:
        print(" ")
        print("=" * 40)
        print("Consulta de Insumos (Producción) - RF 5.1")
        print("=" * 40)
        print("1. Buscar por código")
        print("2. Buscar por nombre")
        print("3. Ver todos")
        print("4. Volver\n")

        opcion = input("Selecciona una opción: ").strip()

        # Buscar por código
        if opcion == "1":
            try:
                codigo_buscar = int(input("Ingresa el código: ").strip())
            except ValueError:
                print("Código inválido.\n")
                continue

            encontrado = False
            for insumo in insumos:
                if insumo.codigo == codigo_buscar:
                    print(insumo)
                    encontrado = True
                    break

            if not encontrado:
                print("\nNo se encontró un insumo con ese código.\n")

        # Buscar por nombre
        elif opcion == "2":
            nombre_buscar = input("Nombre: ").strip().lower()
            encontrados = [i for i in insumos if nombre_buscar in i.nombre]

            if encontrados:
                for insumo in encontrados:
                    print(insumo)
            else:
                print("\nNo se encontraron insumos.\n")

        # Ver todos
        elif opcion == "3":
            for insumo in insumos:
                print(insumo)

        elif opcion == "4":
            print("\nVolviendo al menú de Producción...\n")
            break

        else:
            print("Opción no válida.\n")

#=================================================================================================
# Menú provisional Producción
#=================================================================================================

def menu_produccion():
    while True:
        print("")
        print("=" * 40)
        print("MODULO DE PRODUCCION")
        print("=" * 40)
        print("1. Registrar productos.")
        print("2. Consultar insumos registrados en inventario.")
        print("3. Solicitar insumos para producción.")
        print("4. Volver al menú principal\n")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            Producto.registrar_productos()
        elif opcion == "2":
            consultar_insumos_produccion()
        elif opcion == "3":
            solicitar_insumos(insumos)
        elif opcion == "4":
            print("\nVolviendo al menú principal...\n")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu_produccion()
