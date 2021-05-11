import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import randint

current_page = 1

def invalid_page(page_number):
    response = requests.get(f"https://www.rithmschool.com/blog?page={page_number}")
    soup = BeautifulSoup(response.text, "html.parser")
    p_text_center = soup.find(class_ = "text-center").get_text()
    return p_text_center == 'No matches found'

def scrape_articles(page_number):
    print(f'Processing Page {page_number}')
    response = requests.get(f"https://www.rithmschool.com/blog?page={current_page}")
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all('article')
    with open('blog_datafull.csv', 'a') as csv_file:
        for article in articles:
            a_tag = article.find("a")
            title = a_tag.get_text()
            href = a_tag["href"]
            date = article.find("time")["datetime"]
            csv_writer.writerow([title,href,date])

with open('blog_data_full.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "link", "date"])
    while not invalid_page(current_page):
        scrape_articles(current_page)
        current_page += 1
        sleep(randint(3,8))
