all1 = all([0, 1, 2, 3])  # False as 0 is falsey
all2 = all([char for char in 'eio' if char in 'aeiou'])  # True
all3 = all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0])  # True

people = ["Charlie", "Casey", "Cody", "Carly", "Caristina"]
# True because [True, True, True, True, True]
all([name[0] == 'C' for name in people])

nums = [2, 60, 26, 18]
all([num % 2 == 0 for num in nums])
