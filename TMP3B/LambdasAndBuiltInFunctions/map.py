nums = [2, 4, 6, 8, 10]

# convert doubles map object (iterable only once) to list
doubles = list(map(lambda num: num * 2, nums))

print(nums, doubles)

people = ["Darcy", "Christine", "Dana", "Annabel"]

peeps = list(map(lambda name: name.upper(), people))

print(people, peeps)


def double(x): return x*2


double(3)

dubs = map(double, nums)

print(list(dubs))
