# some_list[start:end:step(interval)] # these are copies

first_list = [1, 2, 3, 4]
slice_index_one = first_list[1:]  # [2, 3, 4]
slice_index_three = first_list[3:]  # [4]
slice_index_negative_one = first_list[-1:]  # [4]
slice_index_negative_three = first_list[-3:]  # [2, 3, 4]
entire = first_list[:]
print('slice from index 1', slice_index_one)
print('slice from index 3', slice_index_three)
print('slice from index negative 1', slice_index_negative_one)
print('slice from index negative 3', slice_index_negative_three)
print('colon is the same as zero', entire)
print('first list array', first_list)

print(first_list == entire)  # same value
print(first_list is entire)  # not same location in memory

until_2 = first_list[:2]  # [1, 2]
until_4 = first_list[:4]  # [1, 2, 3, 4]
from_one_to_three = first_list[1:3]  # [2, 3]
print('until 2', until_2)
print('until 4', until_4)
print('from index 1 to excluding 3', from_one_to_three)

beginning_to_index_negative_one = first_list[:-1]  # [1, 2, 3]
index_one_to_index_negative_one = first_list[1:-1]  # [2, 3]
print('beginning to index negative one (last item)',
      beginning_to_index_negative_one)
print('index 1 to index negative one (last item)',
      index_one_to_index_negative_one)

# second list

second_list = [1, 2, 3, 4, 5, 6]
from_index_one_on_by_two = second_list[1::2]  # [2, 4, 6]
from_beginning_by_two = second_list[::2]  # [1, 3, 5]
print('from index one on by two', from_index_one_on_by_two)
print('from beginning by two', from_beginning_by_two)

start_index_one_minus_one = second_list[1::-1]  # [2, 1]
# [6, 5, 4, 3]
start_from_end_until_index_one_by_minus_one = second_list[:1:-1]
start_index_two_minus_one = second_list[2::-1]  # [3, 2, 1]

print('start from index one, minus one steps', start_index_one_minus_one)
print('start from the end, minus one steps, until index one',
      start_from_end_until_index_one_by_minus_one)
print('start at index two, minus one steps', start_index_two_minus_one)

# tricks with slices

forwards = "This is a string!"
print('fowards', forwards)
print('forwards reverse', forwards[::-1])

numbers = [1, 2, 3, 4, 5]
numbers[1:3] = ['a', 'b', 'c']
print('replace index one to exclusive three with a b c ', numbers)
