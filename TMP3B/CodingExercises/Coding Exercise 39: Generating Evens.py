# Define a function called generate_evens
# It should return a list of even numbers between 1 and 50(not including 50)


def generate_evens():
    evens = []
    for num in range(1, 50):
        if num % 2 == 0:
            evens.append(num)
    return evens


# alt return [x for x in range(1, 50) if x % 2 == 0]
