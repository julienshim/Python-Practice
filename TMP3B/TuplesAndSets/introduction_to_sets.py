# s = set({1, 2, 3, 4, 5, 5, 5})  # {1,2,3,4,5}

# s = set({1, 4, 5})

# s = {1, 4, 5}

# 4 in s  # True
# 8 in s  # FAlse

# s = {1, 4, 5, 4, 5}  # {1, 4, 5}
# s[0]  # Value 's' is unsubscritable

# s = {1, 4, 5, 'a', 'b', 23.3334}  # 1, 'a', 4, 5, 'b', 23.3334} # no way of reference anyway # noqa

# for thing in s:
#     print(thing)

cities = ["Los Angeles", "Boulder", "Kyoto",
          "Flourence", "Santiago", "Los Angeles", "Shanghai", "Boulder", "San Francisco", "Oslo", "Tokyo"]  # noqa

print(len(set(cities)))  # 9
print(set(cities))  # {'Los Angeles', 'Tokyo', 'Oslo', 'Flourence', 'Boulder', 'Shanghai', 'Kyoto', 'San Francisco', 'Santiago'} # noqa
print(list(set(cities)))  # ['Los Angeles', 'Boulder', 'Shanghai', 'Kyoto', 'Oslo', 'Flourence', 'Santiago', 'Tokyo', 'San Francisco'] # noqa
