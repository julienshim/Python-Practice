def interleave(str1, str2):
    return ''.join([''.join(pair) for pair in list(zip(str1, str2))])

# alt dry
    # return ''.join(''.join(x) for x in (zip(str1,str2)))
