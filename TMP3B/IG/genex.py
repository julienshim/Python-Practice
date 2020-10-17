def nums():
    for num in range(1, 10):
        yield num


g = nums()
next(g)

# generator expression
g2 = (num for num in range(1, 10))
next(g2)
