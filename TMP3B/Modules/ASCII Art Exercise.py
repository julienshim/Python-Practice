from pyfiglet import Figlet
from termcolor import colored

valid_colors = ("grey", "red", "green", "yellow",
                "blue", "magenta", "cyan", "white")

user_is_answering = True

while user_is_answering:
    message_is_invalid = True
    while message_is_invalid:
        message = input('What message do you want to print? ')
        if message != '':
            message_is_invalid = False
        else:
            print('You must enter a message!')

    color_is_invalid = True
    while color_is_invalid:
        color = input('What color? ').lower()
        if color not in valid_colors:
            print('Sorry, that color is invalid! Try another color!')
        else:
            color_is_invalid = False

    f = Figlet()
    print(colored(f.renderText(message), color))

    still_continue = True
    while still_continue:
        continue_coloring = input('Do you want to try again? (y/n) ').lower()
        if continue_coloring == 'y' or continue_coloring == 'yes':
            user_is_answering = True
            still_continue = False
        elif continue_coloring == 'n' or continue_coloring == "no":
            user_is_answering = False
            still_continue = False
            print('See you next time!')
        else:
            print('Sorry, I didn\'t get that.')
