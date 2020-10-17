import time
gen_start_time = time.time()
print(sum(n for n in range(1000000000)))
gen_time = time.time() - gen_start_time

list_start_time = time.time()
print(sum([n for n in range(1000000000)]))
list_time = time.time() - list_start_time

print(f"gen_time took {gen_time}")
print(f"list_time took {list_time}")
