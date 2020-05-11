names = ('John', "Jim", "Jerry", "Joseph")

for name in names:
    print(name)

months = ('January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'Ocotober', 'November', 'December')

for month in months:
    print(month)

i = len(months)-1
while i >= 0:
    print(months[i])
    i -= 1

x = (1, 2, 3, 3, 3)
print(x.count(3))
print(x.index(1))

nums = (1, 2, 3, (4, 5), 6, 7)
print(nums)
print(nums[3][1])
print(nums[0:4])
