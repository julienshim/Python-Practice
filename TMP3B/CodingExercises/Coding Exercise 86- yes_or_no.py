'''
gen = yes_or_no()
next(gen) # 'yes'
next(gen) # 'no'
next(gen) # 'yes'
next(gen) # 'no'
'''


def yes_or_no():
    while True:
        yield 'yes'
        yield 'no'
