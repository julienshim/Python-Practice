from keyword import iskeyword


def contains_keyword(*args):
    return True in [iskeyword(n) for n in args]

# alt
    # for item in args:
    #   if keyword(item): return True
