class Animal:
    cool = True

    def make_sound(Self, sound):
        print(f"this animal says {sound}")


class Cat(Animal):
    pass


# a = Animal()
# a.make_sound("CHIRP")

blue = Cat()
# blue.make_sound("MEOW")
# print(blue.cool)
# print(Cat.cool)
# print(Animal.cool)

print(isinstance(blue, Cat))
print(isinstance(blue, Animal))
print(isinstance(blue, object))
