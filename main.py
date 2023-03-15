import json

from Felipe.cat import Cat
from Felipe.Vehicle import Vehicle

from Animal import Animal
from Car import Car

cats = [
    Cat("Whiskers", 3, "Siamese", "White", 5.2, "Male"),
    Cat("Manolo", 2, "Siamese", "Orange", 4.9, "Male"),
    Cat("Andres", 5, "Breed", "Black", 3.7, "Female"),
    Cat("Manolo", 3, "Siamese", "Grey", 5, "Male"),
    Cat("Manolo", 1, "Breed", "White", 0.9, "Female")

]

vehicles = [
    Vehicle("Audi", "A3", "2016", "Red", "5", "Gasoline"),
    Vehicle("Mercedes", "45s", "2018", "Blue", "5", "Gasoline"),
    Vehicle("Seat", "Ibiza", "2019", "White", "5", "Petrol"),
    Vehicle("Renault", "Cactur", "2022", "Perl", "5", "Hybrid"),
    Vehicle("Cupra", "Formentor", "2023", "Black", "5", "Gasoline")
]

cats_list = [c.to_dict() for c in cats]
cars_list = [v.to_dict() for v in vehicles]

data = {"cats": cats_list, "vehicles": cars_list}

with open("JSONAPI/b.json", "w") as file:
    json.dump(data, file)


# Crear lista de 5 instancias de la clase Animal
animal_list = [
    Animal("Luna", 3, "Gato", "Persa", "Negro", 4.5),
    Animal("Toby", 5, "Perro", "Golden Retriever", "Dorado", 28),
    Animal("Nemo", 1, "Pez", "Payaso", "Naranja", 0.1),
    Animal("Kiara", 2, "Gato", "Siames", "Gris", 3),
    Animal("Rocky", 7, "Perro", "Bulldog", "Marron", 25)
]

# Crear lista de 5 instancias de la clase Car
car_list = [
    Car("Ford", "Mustang", 2015, "Rojo"),
    Car("Toyota", "Corolla", 2020, "Negro"),
    Car("BMW", "Serie 3", 2018, "Blanco"),
    Car("Audi", "A4", 2017, "Gris"),
    Car("Chevrolet", "Camaro", 2019, "Amarillo")
]

# Convertir las listas en listas de diccionarios
animal_dict_list = [animal.to_dict() for animal in animal_list]
car_dict_list = [car.to_dict() for car in car_list]

# Guardar las listas de diccionarios en un objeto contenedor
data = {"Animals": animal_dict_list, "Cars": car_dict_list}

# Guardar el objeto contenedor en un archivo .json
with open("json_API/a.json", "w") as outfile:
    json.dump(data, outfile, indent=4)
