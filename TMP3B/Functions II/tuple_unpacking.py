def sum_all_values(*args):
    total = 0
    for num in args:
        total += num
    return total


print(sum_all_values(1, 30, 2, 5, 6))

nums = [1, 2, 3, 4, 5, 6]
# ([1,2,3,4,5,6],) # args if passing list
# ((1,2,3,4,5,6),) # args if passing tuple
print(sum_all_values(*nums))
