from time import sleep
from random import randint

from resources.write_to_csv import write_to_csv
from resources.get_soup import get_quote_soup

targeted_authors =[
    "/author/Albert-Einstein",
    "/author/J-K-Rowling",
    "/author/Jane-Austen",
    "/author/Marilyn-Monroe",
    "/author/Andre-Gide",
    "/author/Thomas-A-Edison",
    "/author/Eleanor-Roosevelt",
    "/author/Steve-Martin",
    "/author/Bob-Marley",
    "/author/Dr-Seuss",
    "/author/Douglas-Adams",
    "/author/Elie-Wiesel",
    "/author/Friedrich-Nietzsche",
    "/author/Mark-Twain",
    "/author/Allen-Saunders",
    "/author/Pablo-Neruda",
    "/author/Ralph-Waldo-Emerson",
    "/author/Mother-Teresa",
    "/author/Garrison-Keillor",
    "/author/Jim-Henson",
    "/author/Charles-M-Schulz",
    "/author/William-Nicholson",
    "/author/Jorge-Luis-Borges",
    "/author/George-Eliot",
    "/author/George-R-R-Martin",
    "/author/C-S-Lewis",
    "/author/Martin-Luther-King-Jr",
    "/author/James-Baldwin",
    "/author/Haruki-Murakami",
    "/author/Alexandre-Dumas-fils",
    "/author/Ernest-Hemingway",
    "/author/Helen-Keller",
    "/author/George-Bernard-Shaw",
    "/author/Charles-Bukowski",
    "/author/Suzanne-Collins",
    "/author/J-R-R-Tolkien",
    "/author/Alfred-Tennyson",
    "/author/Terry-Pratchett",
    "/author/J-D-Salinger",
    "/author/George-Carlin",
    "/author/John-Lennon",
    "/author/W-C-Fields",
    "/author/Ayn-Rand",
    "/author/Jimi-Hendrix",
    "/author/J-M-Barrie",
    "/author/E-E-Cummings",
    "/author/Khaled-Hosseini",
    "/author/Harper-Lee",
    "/author/Madeleine-LEngle"
    ]
 
def next_page_exists(page_number):
    soup = get_quote_soup(page_number)
    return bool(soup.find(class_="next"))

def get_div_text(div):
    quote = div.find(class_="text").get_text()
    author = div.find(class_="author").get_text()
    link = div.find("a")["href"]
    return [quote, author, link]

def get_page_divs(page_number):
    soup = get_quote_soup(page_number)
    quote_divs = soup.find_all(class_="quote")
    for div in quote_divs:
        if div.find("a")["href"] in targeted_authors:
            write_to_csv('a', get_div_text(div))

def process_page(current_page):
    get_page_divs(current_page)
    sleep(randint(3,8))

def scrape_quotes():
    current_page = 0
    while next_page_exists(current_page):
        current_page += 1
        process_page(current_page)