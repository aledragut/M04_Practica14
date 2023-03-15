class Animal:
    def __init__(self, nombre, edad, especie, raza, color, peso):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.raza = raza
        self.color = color
        self.peso = peso

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_especie(self):
        return self.especie

    def get_raza(self):
        return self.raza

    def get_color(self):
        return self.color

    def get_peso(self):
        return self.peso

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_edad(self, edad):
        self.edad = edad

    def set_especie(self, especie):
        self.especie = especie

    def set_raza(self, raza):
        self.raza = raza

    def set_color(self, color):
        self.color = color

    def set_peso(self, peso):
        self.peso = peso

    # Método saludo
    def saludo(self):
        print(f"Hola, me llamo {self.nombre}, soy un/a {self.raza} de {self.edad} años, de color {self.color} y peso {self.peso} kg. Soy de la especie {self.especie}.")

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "especie": self.especie,
            "raza": self.raza,
            "color": self.color,
            "peso": self.peso
        }
