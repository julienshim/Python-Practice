'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
import re

def statistics(input_file):
    tmp = {
        
    }
    with open(input_file) as file:
        content = file.read()
        tmp['lines'] = len(re.split(r"\n", content))
        tmp['words'] = len(re.split(r"\s", content))
        tmp['characters'] = len(content)
    return tmp

# alt 

# def statistics(file_name):
#     with open(file_name) as file:
#         lines = file.readlines()
    
#     return { "lines": len(lines),
#                 "words": sum(len(line.split(" ")) for line in lines),
#                 "characters": sum(len(line) for line in lines) }