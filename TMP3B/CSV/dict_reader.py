from csv import DictReader

with open("fighters.csv") as file:
    csv_reader = DictReader(file)
    for fighter in csv_reader:
        print(fighter['Name'])