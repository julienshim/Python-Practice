# Don't forget to import re!
from re import compile
# Define is_valid_time below:
def is_valid_time(input):
    time_regex = compile(r'\d{1,2}:\d{2}')
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False


## instructor solution

# import re 
    
# def is_valid_time(input):
#     pattern = re.compile(r'^\d\d?:\d\d$')
#     match = pattern.search(input)
#     if match:
#         return True
#     return False