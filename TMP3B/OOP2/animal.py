class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}."

    def make_sound(Self, sound):
        print(f"This animal says '{sound}'.'")


class Cat(Animal):
    def __init__(self, name, breed, toy):
        # Animal.__init__(self, name, species)
        super().__init__(name, species="cat")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


# a = Animal()
# a.make_sound("CHIRP")
blue = Cat("Blue", "Scottish Fold", "string")
# print(blue)
# print(blue.species)
# print(blue.breed)
# print(blue.toy)
blue.play()
# blue.make_sound("MEOW")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

# print(isinstance(blue, Cat))
# print(isinstance(blue, Animal))
# print(isinstance(blue, object))
