'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''

def repeat(s, n):
    return s*n

# alternative

# def repeat(string, num):
#     if (num == 0):
#         return ''
#     i = 0
#     newStr = ''
#     while (i < num):
#         newStr += string
#         i += 1
#     return newStr