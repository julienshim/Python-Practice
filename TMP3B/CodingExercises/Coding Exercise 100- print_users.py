'''
print_users() # None
# prints to the console:
# Colt Steele
'''

from csv import reader

def print_users():
    with open('users.csv') as file:
        csv_reader = reader(file)
        next(csv_reader)
        for person in csv_reader:
            [first_name, last_name] = person
            # print(f"{first_name} {last_name}")
            print("{} {}".format(first_name, last_name)) # for udemy test

# alt

# import csv
    
# def print_users():
#     with open("users.csv") as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader: 
#             print("{} {}".format(row['First Name'], row['Last Name']))