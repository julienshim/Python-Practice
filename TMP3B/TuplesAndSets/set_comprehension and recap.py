print({x**2 for x in range(10)})  # set
print({x: x**2 for x in range(10)})  # dictionary

print({char.upper() for char in 'hello'})


def are_all_vowels_in_string(string):
    # create a set (remember: unique) for char in string if char in vowels. 5 == all unique so all voewls # noqa
    return len({char for char in string if char in 'aeiou'}) == 5


print(are_all_vowels_in_string('sequoia'))
print(are_all_vowels_in_string('hello'))
