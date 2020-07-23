from requests import get
from pyfiglet import figlet_format
from termcolor import colored
from random import choice

# Dad Joke 3000
title_msg = figlet_format("Dad Joke 3000")
title_color = "magenta"
colored_title = colored(title_msg, color=title_color)
print(colored_title)

# Let me tell you a joke! Give me a topic:

topic = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"

header = {
    "Accept": "application/json"
}

param = {
    "term": topic,
}

# I've got 4 jokes about snow. Here's one:

response = get(url, headers=header, params=param)
data = response.json()
jokes = data["results"]

if jokes:
    random = choice(jokes)['joke']
    print(f"I've got {len(jokes)} about {topic}. Here's one: ")
    print(f"{random}")
# Sorry, I don't have any jokes about ____! Please try again.
else:
    print(f"Sorry, I don't have any jokes about {topic}! Please try again.")
