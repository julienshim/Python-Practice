cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True,
}

dog = {"name": "green", "city": "san francisco"}

print('dog before', dog)
dog.update(cat)  # adds cat key value pairs to dog // overwrites existing
print('dog after', dog)

print(cat.pop('name'))  # blue // key must be passed
print(cat)  # name was removed

# random // not arguments can be passed // not a list or dict # noqa
print(cat.popitem())
print(cat)
