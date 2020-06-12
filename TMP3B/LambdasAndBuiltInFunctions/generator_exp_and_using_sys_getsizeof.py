import sys

list_comp = sys.getsizeof([x & 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f'List Comprehension: {list_comp} bytes')  # 9032 bytes
print(f'Generator Expression: {gen_exp} bytes')  # 128 bytes
