# foobar
# print('after the foobar')

# try:
#     foobar
# except NameError:
#     print('PROBLEM')

# print('after the try')

d = {'name': 'Ricky'}


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, 'name'))
print(get(d, 'city'))
