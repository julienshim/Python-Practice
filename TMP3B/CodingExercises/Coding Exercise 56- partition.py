'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def partition(collection, isEven):
    even = [num for num in collection if num % 2 == 0]
    odd = [num for num in collection if num % 2 != 0]
    return [even, odd] if isEven else [odd, even]

# alt1 traditional version
# def partition(lst, fn):
#     trues = []
#     falses = []
#     for val in lst:
#         if fn(val):
#             trues.append(val)
#         else:
#             falses.append(val)
#     return [trues, falses]

# alt2 comprehension
# def partition(lst, fn):
#   return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]] # noqa


# alt another solution
# def partition(l, callback):
    # return [[l.pop(l.index(i)) for i in l if callback(i)], l]
