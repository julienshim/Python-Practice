nums1 = [1, 2, 3, 4, 5]
nums2 = [6, 7, 8, 9, 10]
nums3 = [6, 7, 8, 9, 10, 11, 12]
words = ['hi', 'lol', 'haha', ":)"]

print(list(zip(nums1, nums2)))  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
print(list(zip(nums2, nums1)))  # [(6, 1), (7, 2), (8, 3), (9, 4), (10, 5)]
print(list(zip(nums1, nums3)))  # [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)] # stops at shortest # noqa
print(list(zip(words, nums1, nums3)))  # [('hi', 1, 6), ('lol', 2, 7), ('haha', 3, 8), (':)', 4, 9)] # noqa


print(dict(zip(nums1, nums2)))  # {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
print(dict(zip(nums2, nums1)))  # {6: 1, 7: 2, 8: 3, 9: 4, 10: 5}

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

print(list(zip(*five_by_two)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]
