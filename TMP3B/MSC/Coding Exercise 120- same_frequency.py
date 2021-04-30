'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''

def same_frequency(a, b):
    strA = str(a)
    strB = str(b)
    return all(strA.count(s) == strB.count(s) for s in strA + strB)