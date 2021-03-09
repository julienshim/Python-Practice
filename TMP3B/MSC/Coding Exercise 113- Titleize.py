'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''

def titleize(s):
    arr = s.split(" ")
    arr_list_comp = [x[0].capitalize() + x[1:] for x in arr]
    return ' '.join(arr_list_comp)


# alternative 

# def titleize(string):
#     return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))