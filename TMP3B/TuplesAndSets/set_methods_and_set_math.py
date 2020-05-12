# s = set([1, 2, 3])
# s.add(4)  # {1,2,3,4}
# print(s)
# s.add(4)  # {1,2,3,4}
# print(s)

# another_s = s.copy()
# another_s is s  # false

# cities = {"Los Angeles", "Boulder", "Kyoto",
#           "Flourence", "Santiago", "Los Angeles", "Shanghai", "Boulder", "San Francisco", "Oslo", "Tokyo"}  # noqa
# cities.add("Vancouver")
# print(cities)  # add since no value
# cities.remove("Oslo")  # remove since exists
# print(cities)
# cities.discard("San Antonio")  # avoid errors
# cities.discard("Boulder")

# cities.clear()  # set()

# print("cities", cities)

math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

print(math_students | biology_students)  # set union with unique
print(math_students & biology_students)  # students in both
