from resources.write_headers import write_headers
from resources.scrape_quotes import scrape_quotes
from resources.download_resources import download_resources
from game.banner import banner
from game.class_quote_manager import QuoteManager
from time import sleep

from random import randint, shuffle


download_resources()

print("Loading Game...")
game = QuoteManager()
guesses_remaining = 4
user_is_guessing = True
user_is_in_game = True
user_is_playing_again = False

# game start
print(banner)

# quote
quote = game.get_quote()
quote_author = game.get_quote_author()
answer_list = game.get_answer_arr()

# author_hint
def get_author_hint():
    hint = game.get_author_hint()
    game.navigate_next_hint()
    return hint

def ask_for_a_guess(guesses_remaining):
    return input(f"Who said this? (Guesses remaining: {guesses_remaining}) ")

def give_a_hint():
    print("\nHere's a hint:\n")
    print(f"{get_author_hint()}\n")

def ask_to_play_again():
    user_response = input("Would you like to play again? (Y/N) ")
    confirm = ['y', 'yes']
    decline = ['n', 'no']
    while user_response.lower() not in confirm + decline:
        user_response = input("\nSorry, I didn't get that. Would you like to play again (Y/N)? ")
    if user_response.lower() in confirm:
        return True
    if user_response.lower() in decline:
        return False

while user_is_in_game:
    if user_is_playing_again:
        print("\nGreat! Here we go again...\n")
    print("Here's a quote:\n")
    print(f"{game.get_quote()}\n")
    guess = ask_for_a_guess(guesses_remaining)

    while user_is_guessing:
        if guess not in answer_list: 
            guesses_remaining -= 1
            if guesses_remaining < 1:
                print(f"\nOut of guesses! The author of the quote is {quote_author}.\n")
                user_is_guessing = False
            else:     
                give_a_hint()
                guess = ask_for_a_guess(guesses_remaining)
        if guess in answer_list:
            game.navigate_next_quote()
            print("\nYou guessed correctly! Congratulations!\n")
            user_is_guessing = False
  
    user_is_in_game = ask_to_play_again()
    user_is_playing_again = True
    user_is_guessing = True
    game.navigate_next_quote()
    quote = game.get_quote()
    author = game.get_quote_author()
    answer_list = game.get_answer_arr()
    guesses_remaining = 4

print("\nOk! See you next time!")