# Don't forget to import re!
from re import compile
# Define is_valid_time below:
def is_valid_time(input):
    time_regex = compile(r'\d{1,2}:\d{2}')
    match = time_regex.fullmatch(input)
    if match:
        return True
    return False