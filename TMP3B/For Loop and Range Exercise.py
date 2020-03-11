# Add up all odd numbers between 10 and 20
# Store the result in x:
x = 0


# YOUR CODE GOES HERE:

for num in range(10, 21):
    if (num % 2 == 1):
        x += num
print(x)
