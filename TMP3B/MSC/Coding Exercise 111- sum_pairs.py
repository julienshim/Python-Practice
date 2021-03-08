'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''

def sum_pairs(l, t):
    for i, num in enumerate(l):
        for j, num2 in enumerate(l):
            if i != j:
                if num + num2 == t:
                    return [num, num2]
    return []


# alternative

# def sum_pairs(ints, s):
#     already_visited = set()
#     for i in ints:
#         difference = s - i
#         if difference in already_visited:
#             return [difference, i]
#         already_visited.add(i)
#     return []