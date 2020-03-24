nums = [1, 2, 3]

print([x * 10 for x in nums])  # [10, 20, 30]
print([x / 2 for x in nums])  # [0.5, 1.0, 1.5]

name = 'julien'
print([char.upper() for char in name])  # ['J', 'U', 'L', 'I', 'E', 'N']

friends = ['ashley', 'matt', 'michael']
print([friend[0].upper() + friend[1:]
       for friend in friends])  # ['Ashley', 'Matt', 'Michael']

print([num*10 for num in range(1, 6)])  # [10, 20, 30, 40, 50]

print([bool(val) for val in [0, [], '']])  # [False, False, False]

numbers = [1, 2, 3, 4, 5]
string_numbers = [str(num) for num in numbers]
print(string_numbers)  # ['1', '2', '3', '4', '5']
