# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs


def display_info(a, b, *args, instructor="Matthew", **kwargs):
    return [a, b, args, instructor, kwargs]


print(display_info(1, 2, 3, last_name="Harris", job="Instructor"))
# [1, 2, (3,), 'Matthew', {'last_name': 'Harris', 'job': 'Instructor'}]

# a - 1
# b - 2
# args (3,) # tuple, comma distinguish from parenthesis in single item tuples
# instructor - "Matthew"
# {last_name: 'Harris', 'job: 'Instructor'}
