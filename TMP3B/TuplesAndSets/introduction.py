alphabet = ('a', 'b', 'c', 'd')
print(alphabet)
print(type(alphabet))  # <class 'tuple'>

# alphabet.append('') 'tuple' object has noa ttribute 'append'
# alphabet[0] = 'a' 'tuple' bject does not support item assignment

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'Ocotober', 'November', 'December')

print(months[11], months[4])

locations = {
    (35.6896, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}

print(locations[(37.7749, 122.4194)])

print(locs={[35, 39]: 'Tokyo Office'})  # unhashable type: 'list'

cat = {
    "name": "biscuit", "age": 0.5, "favorite_toy": "my chapstick"
}

type(cat)  # <class 'dict'>
cat.items()  # dict_items([('name', 'biscuit'), ('age', 0.5), ('favorite_toy', 'my chapstick')]) # noqa
