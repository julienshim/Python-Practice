rev = "hello"[::-1]
revd = ''.join(list(reversed('hello')))  # reversed iterator

print(rev, revd)

for x in reversed(range(0, 10)):
    print(x)

for char in reversed("hello world"):
    print(char)
