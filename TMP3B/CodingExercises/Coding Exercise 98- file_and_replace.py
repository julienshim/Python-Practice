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

# alt 

# def find_and_replace(file_name, old_word, new_word):
#     with open(file_name, "r+") as file:
#         text = file.read()
#         new_text = text.replace(old_word, new_word)
#         file.seek(0)
#         file.write(new_text)
#         file.truncate()