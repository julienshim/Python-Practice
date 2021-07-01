'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''

def letter_counter(s):
    def inner(l):
        return s.lower().count(l)
    return inner

# instructor

# def letter_counter(s):
#     letter_counter.val = s
#     def inner(char):
#         return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
#     return inner