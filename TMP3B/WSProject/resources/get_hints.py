from re import compile, findall, sub
from resources.class_author import Author
from resources.get_soup import get_author_soup
from resources.reference_lists import string_sub_pairs, description_string_sub_pairs
from resources.aliases import aliases

def remove_local_unwanted_targets(n, key):
    unwanted_targets = {
        'Alexandre Dumas-fils': ["Her agony"],
        'André Gide': ['by the same ethos'],
        'Charles M. Schulz': ['the syndicate']
    }
    if key in unwanted_targets.keys():
        doesnt_contain_unwanted_targets = not any(map(n.__contains__, unwanted_targets[key]))
        return doesnt_contain_unwanted_targets
    return n

# def correct_period_spacing(string, last_name):
#     return string.replace(f".{last_name}", f". {last_name}")

def sanitize_name(name):
    name = sub("-", " ", name)
    return sub("\.", "", name)

def anonymize_author(string, name, last_name):
    anonymous_pairs = {
        f"{name}'s": "This person's",
        f"{last_name}'s": "This person's",
        f"{name}'": "This person's",
        f"{last_name}'": "This person's",
        f"{name}": "This person",
        f"{last_name}": "This person",
        "His": "This person's",
        "Her": "This person's",
        "He": "This person",
        'She': 'This person'
    }
    for item in anonymous_pairs.keys():
        if string.find(item) == 0:  
            string = sub(item, anonymous_pairs[item], string)
    for n in [name, last_name]:
        string = sub(sanitize_name(n), "this person", string)
    return string[0].upper() + string[1:]

problematic_names_pairs = {
    "Albert Einstein": [
        ('Franklin D. Roosevelt', 'Franklin D Roosevelt'),
        ('Ph.D.', 'PhD')
    ],
    "Charles M. Schulz": [
        ('St. Paul Pioneer Press', 'St Paul Pioneer Press')
    ]
}

local_string_error_pairs = {
    'Charles Bukowski': [
        ('.He died', '. He died'),
        ('\(born as Heinrich Karl Bukowski\) ', ''),
        ('also worked', 'worked')
    ],
    'Ayn Rand': [
        ('.She', '. She'),
        ('also married', 'married')
    ],
    'Allen Saunders': [
        (', John Allen Saunders,', ''),
        (" \(John Phillip Saunders, 1924–2003\),", ",")
    ],
    'Alfred Tennyson': [
        ('plays. he', 'plays. He')
    ],
    'Albert Einstein': [
        ('the word "Einstein"', 'his name'),
        (', however,', ''),
        ('continued to deal', 'dealt'),
        ('also investigated', 'investigated')
    ]
}

def correct_description_string_errors(string, key):
    if key in local_string_error_pairs.keys():
        for pair in local_string_error_pairs[key]:
            [before, after] = pair
            string = sub(before, after, string)
    return string

def problematic_names_prep(string, key):
    if key in problematic_names_pairs.keys():
        for pair in problematic_names_pairs[key]:
            [before, after] = pair
            string = sub(before, after, string)
    return string

def problematic_names_post(string, key):
    if key in problematic_names_pairs.keys():
        for pair in problematic_names_pairs[key]:
            [before, after] = pair
            if after in string:
                string = sub(after, before, string)
    return string      

def sanitize_description_string(string, name):
    if name in aliases.keys():
        for alias in aliases[name]:
            string = sub(alias, sanitize_name(name), string)
    string = correct_description_string_errors(string, name)
    if name in problematic_names_pairs.keys():
        string = problematic_names_prep(string, name)
    regex = compile(r"((?<=[A-Za-z0-9])\.(?=[A-Za-z]{2})|(?<=[A-Za-z]{2})\.(?=[A-Za-z0-9]))")
    return sub(regex, '. ', string)

def target_word_at_start(string, name, last_name):
    name = sanitize_name(name)
    for target in ['He', 'His', 'She', 'Her', last_name]:
        if string.find(target) == 0 or name in string:
            return True
    return False

def determine_last_name(arr):
    if '.' not in arr[len(arr)-1] and arr[len(arr)-1][0].lower() != arr[len(arr)-1][0]:
        return arr[len(arr)-1]
    return arr[len(arr)-2]

def process_description(description_string, name):
    description_string = sanitize_description_string(description_string, name)
    name_arr = sub('-', ' ', name).split(' ')
    last_name = determine_last_name(name_arr)
    regex = compile(r"([\"']?[A-Z][^.?!]+((?![.?!]['\"]?\s[\"']?[A-Z][^.?!]).)+[.?!'\"]+)")
    matches = [m for (m,n) in findall(regex, description_string)]
    matches = list(filter(lambda n: target_word_at_start(n, name, last_name), matches))
    matches = list(filter(lambda n: remove_local_unwanted_targets(n, name), matches))
    # print('\n\n'.join(matches))
    matches = list(map(lambda n: anonymize_author(n, name, last_name), matches))
    if name in problematic_names_pairs.keys():
        matches = list(map(lambda n: problematic_names_post(n, name), matches))
    print('\n\n'.join(matches))
    return matches

def get_hints(link):
    print(link)
    soup = get_author_soup(link)
    name = soup.find(class_="author-title").get_text().split("\n")[0].strip()
    born_date = soup.find(class_="author-born-date").get_text().strip()
    born_location = soup.find(class_="author-born-location").get_text().strip()
    description_arr = process_description(soup.find(class_="author-description").get_text().strip(), name)
    return Author(born_date, born_location, description_arr)