# You can use `bs4` and `requests` to get the data. 

# 1. Grab data on every quote from the website http://quotes.toscrape.com


from resources.write_headers import write_headers
from resources.scrape_quotes import scrape_quotes
from resources.load_resources import load_resources
from resources.get_hints import get_hints
from resources.generate_possible_answers import generate_possible_answers
from game.banner import banner
from time import sleep

from csv import reader
from random import randint, shuffle

with open('./resources/csv/blog_data_full_project.csv') as csv_file:
    csv_reader = reader(csv_file)
    data = [row for row in csv_file]
    if len(data) == 0:
        print('Downloading Game Data...')
        write_headers()
        scrape_quotes()

game_data = load_resources()

print(banner)

position = 0
guesses_remaining = 4
quote = game_data[position].text
author = game_data[position].author
link = game_data[position].link
hints = get_hints(link)
author_alt = hints.name
print(author_alt)
print(hints.get_all_hints())

# while len(hints_four) < 4:
#     hint = hints_all[randint(0, len(hints_all)-1)]
#     if hint not in hints_four:
#         hints_four.append(hint)

# print("Here's a quote:")

# print(quote)

# guess = input(f"Who said this? (Guesses reaminig: {guesses_remaining}) ")

# answer_arr = list(set(generate_possible_answers(author) + generate_possible_answers(hints_all.name)))

# print(answer_arr)


# print("Here's a quote:\n")

# print(f"{quote.text}\n")

# guess = input(f"Who said this? (Guesses remaining: {guesses_left}) ")

# while guess != quote.author

# print(quote.text)
# print(quote.author)
# print(quote.link)

# print(hints.born_date)
# print(hints.born_location)
# print(hints.description_arr)
    
# auths = []



# for i in range(0, len(game_data)):
#     quote = game_data[i]
#     hints = get_hints(quote.link)
#     author = quote.author
#     author_alt = hints.name
#     if author not in auths:
#         answer_arr = list(set(generate_possible_answers(author) + generate_possible_answers(author_alt)))
#         print(answer_arr)
#         auths.append(author)
#         # print('\t'.join([author, author_wo_dash, author_wo_periods_compressed, author_wo_periods_expand, author_unaccented]))
#         sleep(randint(3,8))

# print(hints.get_random_fact())



# if guess.lower() !== quote.author.lower():
#     print("HE")
#     guess = input(f"Who said this? (Guesses remaining: {guesses_left}) ")

# while game_is_running:


# print(quote_divs)

# 2. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.

# 3. Display the quote to the user and ask who said it. The player will have four guesses remaining.

# 4A. After each incorrect guess, the number of guesses remaining will decrement.

# 4B.  If the player gets to zero guesses without identifying the author, the player loses and the game ends.

# 4C. If the player correctly identifies the author, the player wins!





# 6. When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.








# UI



# while guess != answer:
#     if guess:
#         # if

#         # else
#         guess = input(f"")
#     else:
    # enter a guess
# Who said this? Guesses remaining: {n}. <User Input>

# Here's a hint: {Hint}

# Who said this? Guesses remaining: {n}.
# You guessed correctly! Congratulations!
# Would you like to play again (y/n)?


# Great! Here we go again...

# Here's a quote:

#"{quote}"

# Who said this? Guesses remaining: {n}.

# Ok! See you next time!