cat = {
    "name": "blue",
    "age": 3.5,
    "isCute": True,
}

print(cat.get('name'))
print(cat.get('weight'))  # None

kitten = cat.copy()
print(cat == kitten)
print(cat is kitten)

cat.clear()
print(cat)

abc = {}.fromkeys(["a", "b", "c"], "unknown")
a = {}.fromkeys("a", [1, 2, 3, 4, 5])
s = {}.fromkeys('abcdef', "false")
r = {}.fromkeys(range(1, 10), "true")
print(abc)
print(a)
print(s)
print(r)
