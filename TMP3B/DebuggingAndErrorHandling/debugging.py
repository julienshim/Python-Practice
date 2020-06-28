# import pdb  # filename debugging or filename_test

# first = "First"
# second = "Second"
# pdb.set_trace()
# result = first + second
# third = "Third"
# result += third
# print(result)

# Common PDB Commands:
# l (list)
# n (next line)
# p (print)
# c (continue -finished debugging)


def add_numbers(a, b, c, d):  # avoid variable names that conflict with pdb commands # use p <variable> to print # noqa
    import pdb
    pdb.set_trace()  # easy in an out if online
    return a + b + c + d


add_numbers(1, 2, 3, 4)
