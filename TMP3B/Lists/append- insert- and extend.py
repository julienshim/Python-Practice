first_list = [1, 2, 3, 4]
print('first list', first_list)
first_list.append(5)
print('append', first_list)

first_list.extend([6, 7, 8, 9])
print('enxtend', first_list)

first_list.insert(2, 'Hello')  # 2 position
print(first_list)
# below inserts at the last position, which is 9 and doesn't account growth
first_list.insert(-1, "Not quiet last")
print('Not quite last', first_list)

first_list.insert(len(first_list), 'Last')
print('Last is last', first_list)
