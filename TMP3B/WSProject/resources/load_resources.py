from csv import reader

def load_resources():
    with open('resources/csv/blog_data_full_project.csv') as csv_file:
        csv_reader = reader(csv_file)
        return [d for d in csv_reader]