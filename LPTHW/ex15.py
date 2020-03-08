from sys import argv

#python3.7 runs the ex15.py script which takes a file name argument in txt form (e.g. python 3.7 ex15.py ex15.sample.txt)
script, filename = argv

# txt variable set to the open function which open specified filename
txt = open(filename)

#print the string wtih specified file name
print(f"Here's your file {filename}:")

#print the contents of the txt specfied via read method
print(txt.read())

#below same as above but prompt for a txt new file name
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())