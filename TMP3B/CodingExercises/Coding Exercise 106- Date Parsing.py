#import re
from re import compile
#define parse_date below
def parse_date(input):
    date_regex = compile(r'^(?P<d>\d{2})[,/.](?P<m>\d{2})[,/.](?P<y>\d{4})$')
    matches = date_regex.search(input)
    if matches:
        return {
            'd': matches.group('d'),
            'm': matches.group('m'),
            'y': matches.group('y')
        }
    return None


# instructor solve

# import re
    
# def parse_date(input):
#     pattern = re.compile("^(\d\d)[,/.](\d\d)[,/.](\d{4})$")
#     match = pattern.search(input)
#     if match:
#         return {
#             "d": match.group(1),
#             "m": match.group(2),
#             "y": match.group(3),
#         }
#     return None