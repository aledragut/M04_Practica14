class Cat:
    def __init__(self, name, age, breed, color, weight, gender):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color
        self.weight = weight
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_breed(self):
        return self.breed

    def set_breed(self, breed):
        self.breed = breed

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Breed:", self.breed)
        print("Color:", self.color)
        print("Weight:", self.weight)
        print("Gender:", self.gender)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "breed": self.breed,
            "color": self.color,
            "weight": self.weight,
            "gender": self.gender
        }


