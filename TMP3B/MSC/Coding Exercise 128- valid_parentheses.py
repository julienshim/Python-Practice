'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''

def valid_parentheses(s):
    lst = []
    for l in s:
        if l == '(':
            lst.append('(')
        elif l == ')':
            if len(lst) == 0:
                return False
            lst.pop()
    return len(lst) == 0

# instructor 

# def valid_parentheses(parens):
#     count = 0
#     i = 0
#     while i < len(parens):
#         if (parens[i] == '('):
#             count += 1
#         if (parens[i] == ')'):
#             count -= 1
#         if (count < 0):
#             return False
#         i += 1
#     return count == 0