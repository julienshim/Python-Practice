'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(numbers):
    product = 1
    for num in numbers:
        if num % 2 == 0:
            product *= num  # total = total * val (alt)
    return product
