with open('haiku.txt', 'w') as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, goodbye!")

with open('haiku.txt', 'w') as file: # overwrites existing
    file.write("Here's one more haiku\n")
    file.write("What about the older one?\n")
    file.write("Let's go check it out")

with open('lol.txt', 'w') as file:
    file.write('haha' * 10000)

with open('haiku.txt', 'a') as file:
    file.write('\n') # since prev has no \n
    file.write('Appending a new line \n')
    file.write('Appending another new line \n')
    file.write('Appending one more new line')

with open('haiku.txt', 'r+') as file:
    file.write(':)')
    file.seek(10)
    file.write(':(')