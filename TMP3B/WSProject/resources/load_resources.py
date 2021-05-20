from csv import reader
from resources.class_quote import Quote
from random import shuffle

banned_authors = ['/author/Stephenie-Meyer']

def load_resources():
    with open('resources/csv/blog_data_full_project.csv') as csv_file:
        csv_reader = reader(csv_file)
        data = [Quote(quote, author, link) for (quote, author, link) in csv_reader][1:]
        # shuffle(data)
        return data