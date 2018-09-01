from sys import argv

# takes a filename as an argument
script, filename = argv

# either you want to file to be erased or not
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# ? as point to where user can hit ctrl-c or hit return
input("?")

# feedback that txt file will be opened.
print("Opening the file...")
# open the txt file in 'w' or write mode.
target = open(filename, 'w')

#cut the files contents
print("truncating the file. Goodbye!")
target.truncate()

#asking user for three lines with input() prompts following
print("Now I'm going ot ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) #writing line 1
target.write("\n") #new line, etc. etc.
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#closing file.
print("And finally, we close it.")
target.close()