import requests
from bs4 import BeautifulSoup

def get_author_soup(link):
    response = requests.get(link)
    return BeautifulSoup(response.text, "html.parser")

def get_quote_soup(page_number):
    url = f"https://quotes.toscrape.com/page/{page_number}/"
    response = requests.get(url)
    return BeautifulSoup(response.text, "html.parser")