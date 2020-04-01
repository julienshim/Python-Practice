character = {
    "name": "Harry",
    "owns_dog": True,
    "num_spells": 34,
    "fav_lang": "French",
    "is_top10_in_class": True,
    "fav_num": 54
}

for value in character.values():
    print(value)

for key in character.keys():
    print(key)

for key, value in character.items():
    print(f'Key is {key} and value is {value}')
