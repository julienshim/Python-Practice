from re import sub
from resources.sanitize_name import sanitize_name

def anonymize_author(string, name, last_name):
    anonymous_pairs = {
        f"{name}'s": "this person's",
        f"{last_name}'s": "this person's",
        f"{name}'": "this person's",
        f"{last_name}'": "this person's",
        f"{name}": "this person",
        f"{last_name}": "this person",
        "His": "this person's",
        "Her": "this person's",
        "He": "this person",
        'She': 'this person'
    }
    for item in anonymous_pairs.keys():
        if string.find(item) == 0:  
            string = sub(item, anonymous_pairs[item], string)
    for n in [name, last_name]:
        string = sub(sanitize_name(n), "this person", string)
    return string[0].upper() + string[1:]