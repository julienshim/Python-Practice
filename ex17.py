from sys import argv
from os.path import exists

# this app takes in two arguments, the from file and the to file.
script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?

in_file = open(from_file)
indata = in_file.read() #you can simply just do indata = open(from_file).read()

#confirms the size of input file
print(f"The input file is {len(indata)} bytes long")

#checks if to file exists
print(f"Does the output file exist? {exists(to_file)}")
# user prompt to confirm
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

# open to file in write mode and then copy data of in_file onto it
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

#close both files
out_file.close()
in_file.close()