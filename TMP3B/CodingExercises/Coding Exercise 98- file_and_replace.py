'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

def find_and_replace(input_file, target_txt, replace_txt):
    with open(input_file) as file_read:
        content = file_read.read()
        
    with open(input_file, 'w') as file_write:
        new_content = content.replace(target_txt, replace_txt)
        file_write.write(new_content)