from resources.write_to_csv import write_to_csv

def write_headers():
    headers = ["quote", "author", "link"]
    write_to_csv('w', headers)