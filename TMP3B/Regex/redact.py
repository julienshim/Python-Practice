import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) [a-z]+', re.I)
# print(pattern.findall(text)) # ['Mrs.', 'Mr.', 'Ms.'] Searches for first group
# print(pattern.search(text).group()) # Mrs. Daisy Searches for first group
# result = pattern.sub('REDACTED', text)
# print(result)

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
# result = pattern.sub("\g<1> REDACTED", text) # Last night Mrs. REDACTED and Mr. REDACTED murdered Ms. REDACTED
result = pattern.sub("\g<1> \g<2>", text)
print(result)

