'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


def frequency(list, item):
    """
    >>> frequency([1,2,3,4,4,4], 4)
    3
    >>> frequency([True, False, True, True], False)
    1
    """
    return list.count(item)

# alt naming
    # return collection.count(searchTerm)
