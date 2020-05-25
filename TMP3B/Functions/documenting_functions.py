import random


def say_hello():
    """A simple function that returns the string hello"""


print(say_hello.__doc__)  # 'A simple function that returns the string hello'
print(print.__doc__)  # 'Prints the values to a stream, or to sys.stdout by default.' # noqa
print(random.randint.__doc__)  # 'Return random integer in range [a, b], including both end points.' # noqa
print([1, 2, 3].pop.__doc__)  # 'Remove and return item at index (default last).' # noqa
