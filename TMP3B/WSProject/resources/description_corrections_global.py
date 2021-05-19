
from re import sub

general_global_corrections = ['also ', '\n  ', '\n']

def description_corrections_global(string):
    for item in general_global_corrections:
        string = sub(item, '', string)
    return string