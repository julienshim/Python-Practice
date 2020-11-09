'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(collection):
    """
    >>> compact([0,1,2,"",[], False, {}, None, "All done"])
    [1, 2, 'All done']
    """
    return [item for item in collection if bool(item)]

# alt without list comprehension
# def compact(l):
    # truthy_vals = []
    # for val in l:
    #     if val: truthy_vals.append(val)
    # return truthy_vals
