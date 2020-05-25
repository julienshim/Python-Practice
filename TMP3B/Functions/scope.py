instructor1 = 'Marry'


def say_hello():
    instructor2 = 'Bill'
    return f'hello {instructor2}'


say_hello()

print(instructor1)
# print(instructor2)  # Undefined variable 'instructor'

total = 0


def increment():
    global total  # to manipulate global
    total += 1  # local variable 'total' referenced before assignment without global # noqa
    return total


increment()

name = "Rusty"


def greet():
    print(name)


greet()  # works fine


def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()

# now use global nonlocal keyword frequently, but essential to understand scope
