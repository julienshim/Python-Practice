from random import random


def flip_coin():
    # generate random number 0-1
    if random() > 0.5:
        return 'Heads'
    else:
        return 'Tails'

# if a duplicate def flip_coin was here, it would override


print(flip_coin())
