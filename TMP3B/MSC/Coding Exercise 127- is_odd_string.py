'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''

def is_odd_string(string):
    
    alphabet = 'abcdefghijklmnopqrtsuvwxyz'
    
    letter_arr = list(string)
    
    def indesize_letter(letter):
        return alphabet.index(letter) + 1
        
    return sum(map(indesize_letter, letter_arr)) % 2 == 1

# instructor solve

# def is_odd_string(string):
#     total = sum((ord(c) - 96) for c in string.lower()) or 0
#     return total % 2 == 1