from resources.class_author import Author
from resources.get_soup import get_author_soup
from resources.sanitize_name import sanitize_name
from resources.determine_last_name import determine_last_name
from resources.process_raw_description import process_raw_description

def get_hints(link):
    soup = get_author_soup(link)
    name = soup.find(class_="author-title").get_text().split("\n")[0].strip()
    born_date = soup.find(class_="author-born-date").get_text().strip()
    born_location = soup.find(class_="author-born-location").get_text().strip()
    description_arr = process_raw_description(soup.find(class_="author-description").get_text().strip(), name)
    return Author(name, born_date, born_location, description_arr)