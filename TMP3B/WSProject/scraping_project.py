# You can use `bs4` and `requests` to get the data. 
import requests
from bs4 import BeautifulSoup

# 1. Grab data on every quote from the website http://quotes.toscrape.com

current_page = 1
response = requests.get(f"https://quotes.toscrape.com/page/{current_page}/")
soup = BeautifulSoup(response.text, "html.parser")
quote_divs = soup.find_all(class_="quote")
for div in quote_divs:
    quote = div.find(class_="text").get_text()
    author = div.find(class_="author").get_text()
    link = div.find("a")["href"]
    print(link)
# print(quote_divs)

# 2. For each quote you should grab the text of the quote, the name of the person who said the quote, and the href of the link to the person's bio. Store all of this information in a list.

# 3. Display the quote to the user and ask who said it. The player will have four guesses remaining.

# 4A. After each incorrect guess, the number of guesses remaining will decrement.

# 4B.  If the player gets to zero guesses without identifying the author, the player loses and the game ends.

# 4C. If the player correctly identifies the author, the player wins!

# 5A. After every incorrect guess, the player receives a hint about the author. 

# 5B. For the first hint, make another request to the author's bio page, and tell the player the author's birth date and location.

# 5C. The next two hints are up to you! Some ideas: the first letter of the author's first name, the first letter of the author's last name, the number of letters in one of the names, etc.

# 6. When the game is over, ask the player if they want to play again. If yes, restart the game with a new quote. If no, the program is complete.








# UI

# Here's a quote:

# "{quote}"

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