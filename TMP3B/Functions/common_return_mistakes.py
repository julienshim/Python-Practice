# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total  # indentation matters; 1 (in-loop) vs 16 correct.


# print(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7]))

def is_odd_number(num):
    if num % 2 != 0:
        return True
    # else: # uncessary else
    #   return False
    return False


print(is_odd_number(4))
print(is_odd_number(9))
