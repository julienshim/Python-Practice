# answer = [n for n in [1, 2, 3, 4] and [3, 4, 5, 6]
#           if n in [1, 2, 3, 4] and [3, 4, 5, 6]]

answer = [x for x in [1, 2, 3, 4] if x in [3, 4, 5, 6]]  # dry
answer2 = [name[::-1].lower() for name in ["Elie", "Tim", "Matt"]]

print(answer)
