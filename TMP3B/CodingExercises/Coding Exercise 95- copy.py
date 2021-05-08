'''
copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

def copy(input_file, output_file):
    with open(input_file, 'r') as input_file:
        copy = input_file.read()
        with open(output_file, 'w') as outputfile:
            outputfile.write(copy)