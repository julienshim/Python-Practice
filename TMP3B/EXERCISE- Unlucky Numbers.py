for num in range(1, 21):
    if num == 4 or num == 13:
        print(f'{num} is UNLUCKY!')
    elif num % 2 == 1:
        print(f'{num} is odd')
    else:
        print(f'{num} is even')
