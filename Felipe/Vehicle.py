class Vehicle:
    def __init__(self, marca, model, any, color, numeroPuertas, motor):
        self.marca = marca
        self.model = model
        self.any = any
        self.color = color
        self.numeroPuertas = numeroPuertas
        self.motor = motor

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_any(self):
        return self.any

    def set_any(self, any):
        self.any = any

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_numeroPuertas(self):
        return self.numeroPuertas

    def set_numeroPuertas(self, numeroPuertas):
        self.numeroPuertas = numeroPuertas

    def get_motor(self):
        return self.motor

    def set_motor(self, motor):
        self.motor = motor

    def info(self):
        print("Name:", self.name)
        print("model:", self.model)
        print("numero puertas:", self.numeroPuertas)
        print("any:", self.any)
        print("color:", self.color)
        print("motor:", self.motor)

    def to_dict(self):
        return {
            "name": self.marca,
            "model": self.model,
            "numero puertas": self.numeroPuertas,
            "any": self.any,
            "color": self.color,
            "motor": self.motor
        }
