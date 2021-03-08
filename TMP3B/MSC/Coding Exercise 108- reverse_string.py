'''
reverse_string('awesome') # 'emosewa'
reverse_string('Colt') # 'tloC'
reverse_string('Elie') # 'eilE'
'''

# add whatever parameters you deem necessary - good luck!
def reverse_string(s):
    # implement your function here
    return s[::-1]


# alternative

# def reverse_string(str):
#     s = ''
#     for i, char in enumerate(str[::-1]):
#         s += char
#     return s