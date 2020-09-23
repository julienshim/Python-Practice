# Custom For Loop

# for num in [1, 2, 3]:
# for char in "hi there":
# inter()
# next()
# next()


def my_for(iterable, func):
    iterator = iter(iterable)
    while True:
        try:
            thing = next(iterator)
        except StopIteration:
            break
        else:  # else keyword to define block of code to be executed if no errors were raised # noqa
            func(thing)


def square(x):
    print(x * x)


my_for("hello", print)
my_for([1, 2, 3, 4], square)
