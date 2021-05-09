import json

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

c = Cat("Charles", "Tabby")

# j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
j = json.dumps(c.__dict__)

print(j)