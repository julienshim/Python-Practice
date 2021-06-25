# don't forget to import re
from re import compile
# define parse_bytes below:

def parse_bytes(input):
    bytes_regex = compile(r'\b[\d]{8}\b')
    return bytes_regex.findall(input)


## instructor solution

# import re
    
# def parse_bytes(input):
#     binary_regex = re.compile(r'\b[10]{8}\b')
#     results = binary_regex.findall(input)
#     return results