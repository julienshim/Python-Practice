from resources.sub_alias import sub_alias
from resources.description_corrections_local import description_corrections_local
from resources.description_corrections_global import description_corrections_global
from resources.problematic_names import problematic_names_prep
from resources.new_sentence_spacing import new_sentence_spacing

def sanitize_description_string(string, name):
    string = sub_alias(string, name)
    string = description_corrections_local(string, name)
    string = description_corrections_global(string)
    string = problematic_names_prep(string, name)
    string = new_sentence_spacing(string)
    return string