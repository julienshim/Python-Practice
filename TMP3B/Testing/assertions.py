# def add_positive_numbers(x, y):
#     assert x > 0 and y > 0, "Both numbers must be positive."
#     return x + y


# print(add_positive_numbers(1, 1))
# add_positive_numbers(1, -1)  # AssertionError


def eat_junk(food):
    assert food in [
        "pizza",
        "ice cream",
        "candy",
        "fried butter"
    ], "Food must be a junk food."
    return f"Yum. I love {food}."


food = input("Enter a food please: ")
print(eat_junk(food))

# you cannot depend on assert statements
# as a python file ran with -O flag
# will not evaluate assertions
