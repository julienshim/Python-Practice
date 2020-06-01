# def sum_all_nums(num1, num2, num3):
#     return num1+num2+num3


# print(sum_all_nums(4, 6, 9))

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total  # 19


print(sum_all_nums(4, 6, 9))  # (4, 6, 9) tuple


def ensure_correct_info(*args):
    if "Archie" in args and "Hudson" in args:
        return "Welcome back Archie!"
    return "Not sure who you are..."


print(ensure_correct_info())

print(ensure_correct_info(1, True, "Hudson", "Archie"))
