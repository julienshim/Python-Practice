from re import compile, sub, I

def censor(input):
    pattern = compile(r'frack(er|ing)?', I)
    return pattern.sub('CENSORED', input)

## instructor solution

# import re
     
# def censor(input):
#     pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
#     return pattern.sub("CENSORED", input)