insumos = []

#Clase de Insumos:
class Insumo:
    def __init__(self,
                nombre,
                categoria, 
                unidad_medida, 
                stock_actual, 
                stock_minimo, 
                fecha_registro, 
                costo):
        
        self.codigo = len(insumos) + 1001
        self.nombre = nombre
        self.categoria = categoria
        self.unidad_medida = unidad_medida
        self.stock_actual = stock_actual
        self.stock_minimo = stock_minimo
        self.fecha_registro = fecha_registro
        self.costo = costo
        
#Registro de Insumo
    def registrar_insumos():
        unidades_validas = ["litros", "metros", "unidad", "Unidades"]

        while True:
            opcion = input("Deseas registrar un producto (SI/NO): ").strip().lower()

            if opcion == "si":

                nombre_ = input("Ingresa el nombre del insumo: ").strip().lower()
                categoria_ = input("Ingrese la categoria del insumo: ").strip().lower()

                while True:
                    unidad_medida_ = input("Ingrese la unidad de medida del insumo (Litros/Metros/Cantidad): ").strip().lower()
                    if unidad_medida_ in unidades_validas:
                        break
                    else:
                        print("Unidad de medida no válida. Usa Litros, Metros o Unidad/Unidades.")
                
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

                    print("Fecha inválida. Debe estar en formato DD/MM/AAAA y ser una fecha lógica.")

                stock_actual_ = float(input("Ingrese la cantidad que desea ingresar: "))
                stock_minimo_ = float(input("Ingrese el umbral minimo de dicho insumo: "))
                
                while True:
                    costo_ = input("Ingrese el costo el insumo: ").strip()
                    if costo_.isdigit():
                        break
                    else:
                        print("Digita un costo verdadero")


                insumo = Insumo(
                    nombre_,
                    categoria_,
                    unidad_medida_,
                    stock_actual_,
                    stock_minimo_,
                    fecha_registro_,
                    costo_
                )

                insumos.append(insumo)
                print("Insumo registrado correctamente.\n")

            elif opcion == "no":
                print("\nRegistro de insumos finalizado.\n")
                break

            else:
                print("Opción no válida. Responde SI o NO.\n")

    #Metodo de Impresion provicional.
    def __str__(self):
        return (
            f"\nFecha registro: {self.fecha_registro} \nCodigo: {self.codigo} | Nombre: {self.nombre} | Cantidad: {self.stock_actual} {self.unidad_medida} "
            f"- Valor: ${self.costo}."
        )

Insumo.registrar_insumos()

for insumo in insumos:
    print(insumo)
