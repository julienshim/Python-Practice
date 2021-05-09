from csv import reader

with open("fighters2.csv") as file:
    # csv_reader = reader(file)
    csv_reader = reader(file, delimiter="|")
    next(csv_reader) # move past header
    for fighter in csv_reader:
        [name, country, height] = fighter
        print(f"{name} is from {country}")
        # print(row)

# with open("fighters.csv") as file:
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)