'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


def capitalize(name):
    """
    >>> capitalize("tim")
    'Tim'
    >>> capitalize("matt")
    'Matt'
    """
    return name.capitalize()

# alt
    # return string[:1].upper() + string[1:]
