from re import compile, findall, sub
from resources.class_author import Author
from resources.get_soup import get_author_soup
from resources.correct_description_string_errors import correct_description_string_errors
from resources.remove_local_unwanted_targets import remove_local_unwanted_targets
from resources.problematic_names import problematic_names_post, problematic_names_post, problematic_names_pairs
from resources.anonymize_author import anonymize_author
from resources.sanitize_name import sanitize_name
from resources.determine_last_name import determine_last_name
from resources.aliases import aliases

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