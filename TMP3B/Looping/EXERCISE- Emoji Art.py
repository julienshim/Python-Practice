# n = 1
# while n < 11:
#   print("\U0001f600" * n)
#   n += 1

# for num in range(1,11):
#   print("\U0001f600" * num)

# for x in range(3):
#   for num in range(1, 11):
#     print("\U0001f600" * num)

# Without string mulitpilication - UGLY
# for num in range(1,11):
#   count = 1
#   smileys = ""
#   while count < num:
#     smileys += "\U0001f600"
#     count += 1
#   print(smileys)

# centered triangle
n = 1
y = 20 // 2
while n < 20:
  print(" " * y + "\U0001f600" * n)
  n += 2
  y -= 1