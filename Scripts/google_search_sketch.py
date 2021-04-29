import requests # python pip install
import bs4 # python pip install
import time
import random
import csv
import timeit
import re

print('Analyzing TSV...')

output = csv.reader(open('spreadsheet.tsv'), delimiter="\t")

target_keywords = [] # modify

def searchPerson(fn, ln):
    query = f"{fn}+{ln}+keyword+keyword" # modify
    url = "https://google.com/search?q=" + query
    request_results = requests.get(url)
    soup = bs4.BeautifulSoup(request_results.text, "html.parser")
    h3_divs = soup.select('a > h3 > div') # modify for targets
    found = False
    found_list = []
    for pos in range(0, len(h3_divs)):
        headline = str.strip(h3_divs[pos].text)
        if f"{fn} {ln}" in headline and any(map(headline.__contains__, target_keywords)):
            found = True
            found_list.append(headline)
            print(headline)
    if not found:
        print(f"{string} - None")

current = 1

for line in output:
    end = timeit.timeit()
    [first_name, last_name] = line
    searchPerson(first_name, last_name)
    print(f"{current} of ##") # manually enter
    current += 1
    time.sleep(random.randint(3, 7))

