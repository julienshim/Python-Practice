from re import compile, findall, sub
from resources.class_author import Author
from resources.get_soup import get_author_soup
from resources.reference_lists import string_sub_pairs, description_string_sub_pairs
from resources.aliases import aliases

def remove_local_unwanted_targets(n, key):
    unwanted_targets = {
        'Alexandre Dumas-fils': ["Her agony"],
        'André Gide': ['by the same ethos'],
        'Charles M. Schulz': ['the syndicate'],
        'George Bernard Shaw': ['considered it', 'requesting it', 'accepted it'],
        'Haruki Murakami': ['Facebook'],
        'J.K. Rowling': ['the pen name', 'caricature of me', 'based on me'],
        'J.R.R. Tolkien': ['wrote them'],
        'Mark Twain': ['his calling', 'travelogues'],
        'Martin Luther King Jr.': ['he raised public consciousness'],
        'Pablo Neruda': ['pen name was derived']
    }
    if key in unwanted_targets.keys():
        doesnt_contain_unwanted_targets = not any(map(n.__contains__, unwanted_targets[key]))
        return doesnt_contain_unwanted_targets
    return n

def sanitize_name(name):
    name = sub("-", " ", name)
    return sub("\.", "", name)

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

problematic_names_pairs = {
    "Albert Einstein": [
        ('Franklin D. Roosevelt', 'Franklin D Roosevelt'),
        ('Ph.D.', 'PhD')
    ],
    "Charles M. Schulz": [
        ('St. Paul Pioneer Press', 'St Paul Pioneer Press')
    ],
    "Eleanor Roosevelt": [
        ('Franklin D. Roosevelt', 'Franklin D Roosevelt')
    ],
    "Garrison Keillor": [
        ('John Philip Keillor', 'John Philip Keillor'),
        ("St. John's University", "St John's University"),
        ("Mr. Blue", "Mr Blue")
    ],
    "George Bernard Shaw": [
        ("Shaw's Corner", "Shaw's Corner")
    ],
    "Harper Lee": [
        ('Amasa Coleman Lee', 'Amasa Coleman Lee'),
        ('Frances Cunningham Finch Lee', 'Frances Cunningham Finch Lee')
    ],
    "J.K. Rowling": [
        ('J.K. Rowling', 'JK Rowling'),
        ('Peter James Rowling', 'Peter James Rowling'),
        ('Anne Rowling', 'Anne Rowling')
    ],
    "J.R.R. Tolkien": [
        ("C.S. Lewis", 'CS Lewis')
    ],
    "Jimi Hendrix": [
        ('B.B. King', 'BB King')
    ],
    'Jorge Luis Borges': [
        ('J. M. Coetzee', 'J M Coetzee')
    ],
    'Pablo Neruda': [
        ('Jan Neruda', 'Jan Neruda')
    ],
    'Suzanne Collins': [
        ('Shelby Woo', 'S Woo')
    ]
}

local_correction_pairs = {
    "William Nicholson": [
        ('children.from', 'children. From'),
        ('.He lives', '. He lives')
    ],
    "Mother Teresa": [
        ('Blessed Teresa of Calcutta, or ', '')
    ],
    "Mark Twain": [
        (', better known by his pen name Mark Twain,', '')
    ],
    "Marilyn Monroe": [
        ('\(born Norma Jeane Mortenson; June 1, 1926 – August 5, 1962\) ', 'born on June 1, 1926 ')
    ],
    "Madeleine L'Engle": [
        ('.\"Madeleine ', '. Madeleine '),
        ('.\"http', '. Http')
    ],
    'Jorge Luis Borges': [
        ('1986.J. M. Coetzee', '1986. J. M. Coetzee')
    ],
    'John Lennon': [
        (".Lennon revealed", ". Lennon revealed"),
        ("As the group began", "As The Beatles began")
    ],
    'J.R.R. Tolkien': [
        ('2009.Religious', '2009. Religious'),
        ('influencesJ.R.R. Tolkien', 'influences J.R.R. Tolkien'),
        ('Rings\n.Tolkien', 'Rings. Tolkien'),
        (', was born', ' was born'),
    ],
    'J.K. Rowling': [
        ('See also: Robert Galbraith', '')
    ],
    'J.D. Salinger': [
        ('followed Catcher', 'followed his 1951 novel The Catcher in the Rye')
    ],
    'Haruki Murakami': [
        ('.Since childhood', '. Since childhood'),
        ('\(Japanese: 村上 春樹\) ', '')
    ],
    'Harper Lee': [
        ('continued as', 'was')
    ],
    'George R.R. Martin': [
        ('http', 'Http')
    ],
    'George Eliot': [
        ('adopting the nom de plume \"George Eliot,\"', 'adopting a nom de plume,' )
    ],
    'Garrison Keillor': [
        ('\(born Gary Edward Keillor on August 7, 1942 in Anoka, Minnesota\)', 
        'born on August 7, 1942 in Anoka, Minnesota'),
        ('.Keillor was born', '. Keillor was born'),
        ('."In 2004', '. "In 2004'),
        ('\(Keillor also appears in the movie.\)', '')
    ],
    'E.E. Cummings': [
        ('.\”During', '. During'),
        ('source:', 'Source:'),
        ("But, primarily, ", "")
    ],
    'Douglas Adams': [
        ('.In addition', '. In addition'),
        ('other written', 'written'),
    ],
    'Charles Bukowski': [
        ('.He died', '. He died'),
        ('\(born as Heinrich Karl Bukowski\) ', ''),
    ],
    'Ayn Rand': [
        ('.She', '. She'),
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
    ]
}

general_global_corrections = ['also ', '\n  ', '\n']

def correct_description_string_errors(string, key):
    if key in local_correction_pairs.keys():
        for pair in local_correction_pairs[key]:
            [before, after] = pair
            string = sub(before, after, string)
    for item in general_global_corrections:
        string = sub(item, '', string)
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
            name_arr = sub('-', ' ', key).split(' ')
            last_name = determine_last_name(name_arr)
            if after in string:
                string = sub(after, before, string)
            # family sharing the same surname issue
            family_overwrite_error = sub(last_name, 'this person', after)
            if family_overwrite_error in string:
                string = sub(family_overwrite_error, before, string)
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
    print('\n'.join(matches))
    # print(matches)
    return matches

def get_hints(link):
    # print(link)
    soup = get_author_soup(link)
    name = soup.find(class_="author-title").get_text().split("\n")[0].strip()
    born_date = soup.find(class_="author-born-date").get_text().strip()
    born_location = soup.find(class_="author-born-location").get_text().strip()
    description_arr = process_description(soup.find(class_="author-description").get_text().strip(), name)
    return Author(born_date, born_location, description_arr)