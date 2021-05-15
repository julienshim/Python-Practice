from csv import writer

def write_to_csv(mode, items):
    with open('resources/csv/blog_data_full_project.csv', mode) as csv_file:
        csv_writer = writer(csv_file)
        csv_writer.writerow(items)