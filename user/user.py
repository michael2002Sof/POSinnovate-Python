class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return f"User: {self.name} | Username: {self.username}"
