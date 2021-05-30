from resources.write_headers import write_headers
from resources.scrape_quotes import scrape_quotes

from csv import reader

def download_resources():
    with open('./resources/csv/blog_data_full_project.csv') as csv_file:
        csv_reader = reader(csv_file)
        data = [row for row in csv_file]
        if len(data) == 0:
            print('Downloading Game Data...')
            write_headers()
            scrape_quotes()