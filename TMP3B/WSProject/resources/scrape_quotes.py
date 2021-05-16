from time import sleep
from random import randint

from resources.write_to_csv import write_to_csv
from resources.get_soup import get_quote_soup
 
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
        write_to_csv('a', get_div_text(div))

def process_page(current_page):
    print("*" * current_page)
    get_page_divs(current_page)
    sleep(randint(3,8))

def scrape_quotes():
    current_page = 0
    while next_page_exists(current_page):
        current_page += 1
        process_page(current_page)