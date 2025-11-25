from datetime import datetime

#Comentariado excelente por si algun moya me pregunta 
class SaleItem:
    def __init__(self, product, quantity, unit_price):
        self.product = product                             #en esta clase se calcula el subtotal del producto a vender
        self.quantity = quantity    
        self.unit_price = unit_price
        self.subtotal = quantity * unit_price

#esta ya es la clase completa donde aparecen todos los datos que se necesitan para registrar la venta
class Sale:
    def __init__(self, code, date, customer_name, items, payment_method):
        self.code = code
        self.date = date or datetime.now().strftime("%d/%m/%Y %H:%M")
        self.customer_name = customer_name                                 
        self.items = items          # lista de SaleItem
        self.payment_method = payment_method
        self.status = "registrada"
        self.total = sum(item.subtotal for item in items)   #ya se que hay un subtotal pero si hay mas de un articulo y cantidad etc se calcula tmb
                                                            
    def __str__(self):            #Tambien le puse str porque me gusto como se ve
        lineas = []
        lineas.append("============================================================")
        lineas.append(f"VOUCHER DE VENTA #{self.code}")
        lineas.append(f"Fecha y hora: {self.date}")
        lineas.append(f"Cliente: {self.customer_name}")
        lineas.append(f"Estado: {self.status}")
        lineas.append("------------------------------------------------------------")
        lineas.append("Detalle de productos:")

        for item in self.items:
            p = item.product
            lineas.append(
                f"- [{p.codigo}] {p.marca} {p.modelo} {p.tipo} T{p.talla} {p.color} | "
                f"Cant: {item.quantity} | PU: ${item.unit_price} | Subtotal: ${item.subtotal}"
            )

        lineas.append("------------------------------------------------------------")
        lineas.append(f"TOTAL A PAGAR: ${self.total}")
        lineas.append(f"Forma de pago: {self.payment_method}")
        lineas.append("============================================================")

        return "\n".join(lineas)