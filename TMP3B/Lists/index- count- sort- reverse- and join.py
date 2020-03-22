# numbers = [5, 6, 7, 8, 9, 10]
# where_is_six = numbers.index(6)  # 1
# where_is_nine = numbers.index(9)  # 4
# print('where is six', where_is_six)
# print('where is nine', where_is_nine)

numbers = [5, 5, 6, 7, 5, 8, 8, 9, 10]
where_is_five = numbers.index(5)
where_is_five_from_index_one = numbers.index(5, 1)  # 1
where_is_five_from_index_two = numbers.index(5, 2)  # 4
where_is_eight_from_index_six_through_eight = numbers.index(8, 6, 8)  # 6
print("numbers", numbers)
print("where is five from the numbers array", where_is_five)
print("where is five from index 1 on", where_is_five_from_index_one)
print("where is five from index 2 on", where_is_five_from_index_two)
print("where is eight from index six through eight",
      where_is_eight_from_index_six_through_eight)


how_many_five = numbers.count(5)  # 3
print('how many fives', how_many_five)

numbers.reverse()
print("reverse", numbers)

numbers.sort()
print("sort", numbers)  # capitals come before in alpha

words = ['Coding', 'is', 'fun']
together = ' '.join(words)
print(f'joining {words} equals: ', together)
