f = open('story_2.txt')
# print(f.read())
# print(f.read()) # ''
# print(f.seek(0))
# print(f.read())
# print(f.read()) # ''
# print(f.seek(1))
# print(f.read()) # ''

# print(f.readline()) # This short story is really short.
# print(f.readline()) # Now it's a little longer.
# print(f.readline()) # The end.

print(f.readlines()) # ['This short story is really short.\n', "Now it's a little longer.\n", 'The end.']

# print(f.read()) # ''
print(f.closed)
f.close()
print(f.closed)