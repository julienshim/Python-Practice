instructor = {
    'name': 'bill',
    'city': 'los angeles',
    'color': 'purple'
}

yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}
# print(yelling_instructor)

color_instructor = {(k.upper() if k == 'color' else k): v.upper()
                    for k, v in instructor.items()}
print(color_instructor)


num_list = [1, 2, 3, 4]

odd_even = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
# print(odd_even)

hundred = {num: ("even" if num % 2 == 0 else "odd") for num in range(0, 100)}
# print(hundred)
