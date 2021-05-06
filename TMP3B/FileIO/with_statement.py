# file = open('story_2.txt')
# file.read()
# file.close()

# file.closed # True

# with open('story_2.txt') as file:
#     file.read()

# file.closed # True

with open('story_2.txt') as f:
    data = f.read()
    f.close()
    print(data)

print(f.closed) # True
