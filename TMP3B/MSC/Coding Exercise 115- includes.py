'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''

def includes(a, *args):
    val = args[0]
    if isinstance(a, list) or isinstance(a, str):
        arr = a[args[1]:] if len(args) > 1 else a
        return val in arr
    elif isinstance(a, dict):
        return val in a.values()

# None
# def includes(item,val,start=None):
#     if type(item) == dict:
#         return val in item.values()
#     if start is None:
#         return val in item
#     return val in item[start:]