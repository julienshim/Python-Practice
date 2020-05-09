list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# make sure your solution is assigned to the answer variable so the tests can work! # noqa
answer = {list1[val]: list2[val] for val in range(0, len(list1))}

# dict(zip(list1,list2))  # covered later in course
