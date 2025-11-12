class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Customer: {self.name} | Email: {self.email} | Phone: {self.phone}"
