from re import compile, sub, I

def censor(input):
    pattern = compile(r'frack(er|ing)?', I)
    return pattern.sub('CENSORED', input)
