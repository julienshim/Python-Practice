from re import compile, findall

def find_sentences(string):
    regex = compile(r"([\"']?[A-Z][^.?!]+((?![.?!]['\"]?\s[\"']?[A-Z][^.?!]).)+[.?!'\"]+)")
    return [m for (m,n) in findall(regex, string)]