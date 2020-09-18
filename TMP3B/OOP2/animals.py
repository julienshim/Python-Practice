class Aquatic:
    def __init__(self, name):
        print("aquatic")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming."

    def greet(self):
        return f"I am {self.name} of the sea!"


class Ambulatory:
    def __init__(self, name):
        print("ambulatory")
        self.name = name

    def walk(self):
        return f"{self.name} is walking."

    def greet(self):
        return f"I am {self.name} of the land!"


class Penguin(Ambulatory, Aquatic):
    def __init(self, name):
        print("penguin")
        super().__init__(name=name)


# jaws = Aquatic("Janws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

# print(captain_cook.swim())
# print(captain_cook.walk())
# print(captain_cook.greet())

# print(f"captain_cook is instance of Peguin: {isinstance(captain_cook, Penguin)}")  # noqa
# print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")  # noqa
# print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")  # noqa
