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

        self.estado = "disponible" if self.cantidad > 0 else "agotado"

    def registrar_productos():
        tipos_validos = ["deportivo", "casual", "formal", "sandalia", "bota"]

        while True:
            opcion = input("¿Deseas registrar un producto (SI/NO)?: ").strip().lower()

            if opcion == "si":

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
                        print("Tipo no válido.\n")

                #Validación estricta de talla (36–45)
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

            elif opcion == "no":
                print("\nRegistro de productos finalizado.\n")
                break

            else:
                print("Opción no válida. Responde SI o NO.\n")

    #Metodo de impresion provicional
    def __str__(self):
        return (
            f"Fecha: {self.fecha_registro}:\n"
            f"Codigo: {self.codigo} | Marca: {self.marca} | Género: {self.genero}.\n"
            f"Modelo: {self.modelo} - Tipo: {self.tipo} - Talla: {self.talla}.\n"
            f"Color: {self.color} - Cantidad: {self.cantidad} pares - "
            f"Precio: ${self.precio_venta} - Estado: {self.estado}." 
        )

Producto.registrar_productos()

# Mostrar todos los productos registrados
for producto in productos:
    print(producto)
