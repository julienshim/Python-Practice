'''
truncate("Super cool", 2) # "Truncation must be at least 3 characters."
truncate("Super cool", 1) # "Truncation must be at least 3 characters."
truncate("Super cool", 0) # "Truncation must be at least 3 characters."
truncate("Hello World", 6) # "Hel..."
truncate("Problem solving is the best!", 10) # "Problem..."
truncate("Another test", 12) # "Another t..."
truncate("Woah", 4) # "W..."
truncate("Woah", 3) # "..."
truncate("Yo",100) # "Yo"
truncate("Holy guacamole!", 152) # "Holy guacamole!"
'''

def truncate(s, n):
    if n > len(s):
        return s
    elif n >= 3:
        return s[0:(n-3)] + '...' # the test doesn't recognize f-strings
    return "Truncation must be at least 3 characters."


# alternative

# def truncate(string, n):
#     if (n < 3):
#         return "Truncation must be at least 3 characters."
#     if (n > len(string) + 2):
#         return string

#     return string[:n - 3] + "..."