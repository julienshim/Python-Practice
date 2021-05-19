from re import compile, sub

def new_sentence_spacing(string):
    regex = compile(r"((?<=[A-Za-z0-9])\.(?=[A-Za-z]{2})|(?<=[A-Za-z]{2})\.(?=[A-Za-z0-9]))")
    return sub(regex, '. ', string)