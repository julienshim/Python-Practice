from re import compile, findall, sub
from resources.sanitize_description_string import sanitize_description_string
from resources.target_word_at_start import target_word_at_start
from resources.unwanted_target_removeal_local import unwanted_target_removeal_local
from resources.anonymize_author import anonymize_author
from resources.problematic_names import problematic_names_post
from resources.determine_last_name import determine_last_name
from resources.find_sentences import find_sentences

def process_raw_description(description_string, name):
    description_string = sanitize_description_string(description_string, name)
    last_name = determine_last_name(name)
    matches = find_sentences(description_string)
    matches = list(filter(lambda n: target_word_at_start(n, name, last_name), matches))
    matches = list(filter(lambda n: unwanted_target_removeal_local(n, name), matches))
    matches = list(map(lambda n: anonymize_author(n, name, last_name), matches))
    matches = list(map(lambda n: problematic_names_post(n, name), matches))
    print('\n'.join(matches))
    return matches