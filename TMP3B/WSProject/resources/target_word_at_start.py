from resources.sanitize_name import sanitize_name

def target_word_at_start(string, name, last_name):
    for target in ['He', 'His', 'She', 'Her', last_name]:
        if string.find(target) == 0 or sanitize_name(name) in string:
            return True
    return False