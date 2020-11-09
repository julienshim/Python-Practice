'''
is_palindrome('testing') # False
is_palindrome('tacocat') # True
is_palindrome('hannah') # True
is_palindrome('robert') # False
is_palindrome('amanaplanacanalpanama') # True
'''


def is_palindrome(string):
    """
    >>> is_palindrome('testing')
    False
    >>> is_palindrome('tacocat')
    True
    >>> is_palindrome('hannah')
    True
    >>> is_palindrome('robert')
    False
    >>> is_palindrome('amanaplanacanalpanama')
    True
    """
    strip = string.lower().strip()
    return strip == strip[::-1]

# alt1 - without whitespace removal
    # return string == string[::-1]

# alt2
    # stripped = string.replace(" ", "")
    # return stripped == stripped[::-1]
