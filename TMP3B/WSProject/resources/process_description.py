from re import compile, findall, sub
from resources.sanitize_description_string import sanitize_description_string
from resources.target_word_at_start import target_word_at_start
from resources.remove_local_unwanted_targets import remove_local_unwanted_targets
from resources.anonymize_author import anonymize_author
from resources.problematic_names import problematic_names_post
from resources.determine_last_name import determine_last_name

def process_description(description_string, name):
    description_string = sanitize_description_string(description_string, name)
    name_arr = sub('-', ' ', name).split(' ')
    last_name = determine_last_name(name_arr)
    regex = compile(r"([\"']?[A-Z][^.?!]+((?![.?!]['\"]?\s[\"']?[A-Z][^.?!]).)+[.?!'\"]+)")
    matches = [m for (m,n) in findall(regex, description_string)]
    matches = list(filter(lambda n: target_word_at_start(n, name, last_name), matches))
    matches = list(filter(lambda n: remove_local_unwanted_targets(n, name), matches))
    matches = list(map(lambda n: anonymize_author(n, name, last_name), matches))
    matches = list(map(lambda n: problematic_names_post(n, name), matches))
    print('\n'.join(matches))
    return matches