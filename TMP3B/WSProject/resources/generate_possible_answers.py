from re import sub
from unidecode import unidecode

def generate_possible_answers(name):
    name_wo_dash = sub('-', ' ', name)
    name_wo_periods_compressed = sub('\.', '', name)
    name_wo_periods_expand = sub('  ', ' ', sub('\.', ' ', name))
    name_w_periods_expand = sub('  ', ' ', sub('\.', '. ', name))
    name_unaccented = unidecode(name)
    name_list = list(map(lambda x: x.strip(), [name, name_wo_dash, name_wo_periods_compressed, name_wo_periods_expand, name_w_periods_expand, name_unaccented]))
    if name == "Thomas A. Edison":
        name_list.append("Thomas Edison")
    return name_list