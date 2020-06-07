def display_names(first, second):
    return f'{first} says hello to {second}'


names = {"first": "Colt", "second": "Rusty"}

print(display_names(first="Charlie", second="Sue"))
# print(display_names(names)) # display_names() missing 1 required positional argument: 'second' # noqa

print(display_names(**names))  # first='Colt', second ='Rusty'


def add_and_multiply_numbers(a, b, c):  # , **kwargs {}
    return a+b*c


data = dict(a=1, b=2, c=3)

print(add_and_multiply_numbers(**data))  # 7 #, cat="blue" in {} if **kwargs
