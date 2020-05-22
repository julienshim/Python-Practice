def full_name(first, last):
    return f"Your name is {first} {last}."


print(full_name(first='John', last='Doe'))  # Your name is John Doe.
print(full_name(last='Doe', first='John'))  # Your name is John Doe.


def exponent(num, power=2):
    return num ** power


print(exponent(power=3, num=4))  # 64
print(exponent(num=4, power=3))  # 64
