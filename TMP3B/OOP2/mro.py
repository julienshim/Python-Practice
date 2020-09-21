class A:
    def do_something(self):
        print("Method Defined In: A")


class B(A):
    # pass
    def do_something(self):
        print("Method Defined In: B")


class C(A):
    # pass
    def do_something(self):
        print("Method Defined In: C")


class D(B, C):
    # pass
    def do_something(self):
        print("Method Defined In: D")
        super().do_something()


# print(D.__mro__)
# print(D.mro())
# help(D)
thing = D()
thing.do_something()

# D -> B -> C -> A -> Object
