class Chicken:
    total_eggs = 0

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.eggs = 0

    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        # return self.eggs
