def divide(num1, num2):
    try:
        return num1 / num2
    except TypeError:
        return 'Please provide two integers or floats'
    except ZeroDivisionError:
        return 'Please do not divide by zero'


divide(4, 2)  # 2
divide([], "1")  # "Please provide two integers or floats"
divide(1, 0)  # "Please do not divide by zero"

# alt

# def divide(a,b):
#     try:
#         total = a / b
#     except TypeError:
#         return "Please provide two integers or floats"
#     except ZeroDivisionError:
#         return "Please do not divide by zero"
#     return total
