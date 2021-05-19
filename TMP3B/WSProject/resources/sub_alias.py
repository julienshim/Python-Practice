from re import sub
from resources.sanitize_name import sanitize_name

aliases = {
    'E.E. Cummings': ['Edward Estlin Cummings', 'Mr. Cummings'],
    'Eleanor Roosevelt': ['Anna Eleanor Roosevelt'],
    'Charles Bukowski': ['Henry Charles Bukowski'],
    'George Eliot': ['novelist George Eliot \(nee Mary Ann Evans\),'],
    'J.D. Salinger': ['Jerome David Salinger'],
    'J.R.R. Tolkien': ['John Ronald Reuel Tolkien'],
    'John Lennon': ['John Winston Ono Lennon'],
    'Mark Twain': ['Samuel Langhorne Clemens'],
    'Steve Martin': ['Stephen Glenn "Steve" Martin'],
    "Terry Pratchett": ['Sir Terry Pratchett']
}

def sub_alias(string, name):
    if name in aliases.keys():
        for alias in aliases[name]:
            string = sub(alias, sanitize_name(name), string)
    return string