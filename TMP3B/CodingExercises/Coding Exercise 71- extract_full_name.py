'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}] # noqa
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


def extract_full_name(names):
    return list(map(lambda n: '{} {}'.format(n['first'], n['last']), names))
