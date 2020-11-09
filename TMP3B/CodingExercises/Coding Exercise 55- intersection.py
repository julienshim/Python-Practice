
# flesh out intersection pleaseeeee


def intersection(la, lb):
    """
    >>> intersection([1,2,3],[2,3,4])
    [2, 3]
    >>> intersection(['a','b','z'], ['x','y','z'])
    ['z']
    """
    return list(set(la) & set(lb))

# alt - manual looping
# def intersection(l1, l2):
#     in_common = []
#     for val in l1:
#         if val in l2:
#             in_common.append(val)
#     return in_common

# alt list comprehension solution
# def intersection(l1, l2):
#     return [val for val in l1 if val in l2]

# alt sets solution
# def intersection(list1, list2):
#     return [val for val in set(list1) & set(list2)]
