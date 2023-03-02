class Token:
    def __init__(self, type, value, literal):
        self.type = type
        self.value = value
        self.literal = literal

    def __str__(self):
        return f'{self.type.capitalize()}: "{self.value}"'
