from sys import argv

script, input_file = argv


def print_all(f):  # f is a vairable for file.
    print(f.read())


def rewind(f):
    f.seek(0)  # move to the start of the file in bytes, so 0 bytes not line 0


def print_a_line(line_count, f):
    print(line_count, f.readline())  # print line number, then line text
    # advance line
    # print new line number, then line text
    # basically looping to end of text.


current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
