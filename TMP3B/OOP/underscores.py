# _name #
# __name #
# __name__


class Person:
    def __init__(self):  # don't define your own methods; for overwriting python methods # noqa
        self.name = "Tony"
        # this is 'supposed' to be private but no such thing in python; not intended to use # noqa
        self._secret = "hi!"
        self.__msg = "I like cats!"  # name mangling to _Person__msg
        self.__lol = "HAHAHAHAHA!"  # name mangling to _Person__lol


p = Person()

print(p.name)
print(p._secret)
# print(p.__msg)
print(dir(p))
