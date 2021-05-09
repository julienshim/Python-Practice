# python3 -m pip install jsonpickle

import jsonpickle

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

# c = Cat("Charles", "Tabby")

# frozen = jsonpickle.encode(c)
# print(frozen) # {"py/object": "__main__.Cat", "breed": "Tabby", "name": "Charles"}

# with open('cat.json', 'w') as file:
#     frozen = jsonpickle.encode(c)
#     file.write(frozen)

with open('cat.json', 'w') as file:
    contents = file.read()
    unfrozen = jsonpickle.decode(contents)
    print(unfrozen)