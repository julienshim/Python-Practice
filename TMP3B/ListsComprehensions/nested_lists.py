# nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(nested_lists[0][1])  # 2
# print(nested_lists[1][-1])  # 6

# # for l in nested_lists:
# #     for val in l:
# #         print(val)

# [[print(val) for val in l] for l in nested_lists]

board = [[n for n in range(1, 4)] for v in range(1, 4)]
print(board)

board = [['X' if n % 2 != 0 else 'O' for n in range(
    1, 4)] for v in range(1, 4)]
print(board)
