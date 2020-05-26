'''
last_element([1,2,3]) # 3
last_element([]) # None
'''


def last_element(arr):
    return arr.pop() if len(arr) > 0 else None

# alt

# def last_element(l):
#     if l:
#         return l[-1]
#     return None
