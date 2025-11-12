class Sale:
    def __init__(self, customer, products):
        self.customer = customer
        self.products = products
        self.total = sum([product.price for product in products])

    def __str__(self):
        products_str = "\n".join([f"- {product}" for product in self.products])
        return f"Sale:\nCustomer: {self.customer}\nProducts:\n{products_str}\nTotal: {self.total}"