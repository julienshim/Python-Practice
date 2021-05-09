'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

from csv import reader

def find_user(first_name, last_name):
    with open('users.csv') as file:
        csv_reader = reader(file)
        for index, person in enumerate(csv_reader):
            # if ' '.join(person) == f"{first_name} {last_name}":
            if ' '.join(person) == "{} {}".format(first_name, last_name): # udemy testing
                return index
        return 'Not Here not found.'

# alt - not sure how this follows instructions

# import csv
    
# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)