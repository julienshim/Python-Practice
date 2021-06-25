from re import compile

def extract_phone(input):
    phone_regex = compile(r'\b\d{3} \d{3}-\d{4}\b')
    match = phone_regex.search(input)
    if match:
        return match.group()
    return None

# print(extract_phone("My number is 415 555-2424"))
# print(extract_phone("My number is 415 555-242422"))
# print(extract_phone("sssssss 415 555-2424"))
# print(extract_phone("415 555-2424"))

def extract_all_phones(input):
    phone_regex = compile(r'\b\d{3} \d{3}-\d{4}\b')
    return phone_regex.findall(input)

# print(extract_all_phones("My number is 415 555-2424 or call me at 510 555-2424"))

# def is_valid_phone(input):
#     phone_regex = compile(r'^\d{3} \d{3}-\d{4}\b$') 
#     match = phone_regex.search(input)
#     if match:
#         return match.group()
#     return False

def is_valid_phone(input):
    phone_regex = compile(r'\d{3} \d{3}-\d{4}\b') 
    match = phone_regex.fullmatch(input)
    if match:
        return match.group()
    return False

print(is_valid_phone("415 555-2424"))
print(is_valid_phone("My number is 415 555-2424"))
print(is_valid_phone("My number is 415 555-2424 or call me at 510-55-2424"))
