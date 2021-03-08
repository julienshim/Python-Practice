'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''

def vowel_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_dict = {}
    
    for i, x in enumerate(s):
        s_lowercase = s.lower()
        if x in vowels and x not in vowels_dict and s_lowercase.count(x) > 0:
            vowels_dict[x] = s_lowercase.count(x)
            
    return vowels_dict

# alternative 

# def vowel_count(string):
#     lower_s = string.lower()
#     return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}