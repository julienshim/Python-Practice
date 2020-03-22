first_list = [1, 2, 3, 4]
print('first list', first_list)
first_list.pop()  # remove last
print('pop last', first_list)
first_list.pop(0)
print('pop index 0', first_list)
blah = first_list.pop()
print('variable to pop', blah, first_list)  # 3, [2]
first_list.clear()
print('clear', first_list)


second_list = [1, 2, 3, 4]
# remove first instance of 2
second_list.remove(2)
# remove first instance of 4
second_list.remove(4)
