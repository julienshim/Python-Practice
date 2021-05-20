from re import sub
from resources.determine_last_name import determine_last_name

problematic_names_pairs = {
    "Albert Einstein": [
        ('Franklin D. Roosevelt', 'Franklin D Roosevelt'),
        ('Ph.D.', 'PhD')
    ],
    "Alfred Tennyson": [
        ('George Tennyson', 'George Tennyson')
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
    "George R.R. Martin": [
        ('Raymond Collins Martin', 'Raymond Collins Martin'),
        ('Margaret Brady Martin', 'Margaret Brady Martin'),
        ('Darleen Martin Lapinsk', 'Darleen Martin Lapinsk'),
        ('Janet Martin Patten', 'Janet Martin Patten')
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
    'Ralph Waldo Emerson': [
        ('Henry David Thoreau', 'H David Thoreau')
    ],
    'Suzanne Collins': [
        ('Shelby Woo', 'S Woo')
    ],
    'William Nicholson': [
        ('Map of the Heart', 'Map of the H')
    ]
}

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
            last_name = determine_last_name(key)
            if after in string:
                string = sub(after, before, string)
            # name sharing issue
            family_overwrite_error = sub(last_name, 'this person', after)
            if family_overwrite_error in string:
                string = sub(family_overwrite_error, before, string)
    return string    