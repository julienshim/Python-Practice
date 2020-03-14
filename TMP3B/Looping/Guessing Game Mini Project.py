import random

user_is_playing = True

while user_is_playing:

    random_number = random.randint(1, 10)  # numbers 1 - 10

    is_running = True

    while(is_running):
        # handle user guesses
        user_guess = int(input('Guess a number between 1 and 10: '))
        #   if they guess correct, tell them they won
        if random_number == user_guess:
            print('You guessed it! You won!')
            is_running = False
        elif user_guess < 1 or user_guess > 10:
            print('That\'s not a number between 1 and 10! Try again!')
        #  otherwise tell them if they are too high or too low
        elif user_guess > random_number:
            print('Too high, try again!')
        else:
            print('Too low, try again!')

    # BONUS - let player play again if they want!
    continue_game = input('Do you want to keep playing? (y/n) ').lower()

    if continue_game == 'n':
        user_is_playing = False
    elif continue_game == 'y':
        user_is_playing = True
    else:
        continue_game = input(
            'Sorry, I didn\'t get that. Do you want to keep playing (y/n) ')


print('Thanks for playing!')
