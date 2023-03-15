class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # Getters
    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    # Setters
    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_color(self, color):
        self.color = color

    def salutacio(self):
        print(f"Hola, sóc un {self.make} {self.model} del {self.year} i sóc de color {self.color}.")
    def to_dict(self):
        car_dict = {
            'make': self.make,
            'model': self.model,
            'year': self.year,
            'color': self.color
        }
        return car_dict
