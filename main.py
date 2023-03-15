import json

from Felipe.cat import Cat
from Felipe.Vehicle import Vehicle

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
