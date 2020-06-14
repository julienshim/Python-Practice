import math

print(abs(-23))  # 23
print(abs(3.444))  # 3.444
print(abs(-3.444))  # 3.444
print(abs(float('20')))  # 20.0

print(math.fabs(-4))  # 4.0

print(sum([1, 2, 3]))  # 6
print(sum([1, 2, 3], 10))  # 16
print(sum([1, 2, 3], -6))  # 0
print(sum([1.5, 2, 3.7]))  # 7.2
print(sum({1, 50, 100}))  # 151

# math.fsum for extra floating point precision

# print(sum(['hi', 'there'], 'lol'))  # suggests ''.join(seq) per docs

print(round(10.2))  # 10
print(round(1.212121, 2))  # 1.21
print(round(3.51234))  # 4
print(round(3.51234, None))  # 4
print(round(3.51234, 3))  # 3.512
print(round(9.999999999999999999999999999, 15))  # 10.0
