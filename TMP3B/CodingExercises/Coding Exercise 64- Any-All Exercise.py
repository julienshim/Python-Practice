# Implement your is_all_strings function below:
def is_all_strings(l):
    return all(type(i) == str for i in l)

# alt list comprehension
    # return all([type(i) == str for i in l])
