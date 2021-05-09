'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''

from csv import writer

def add_user(first_name, last_name):
    with open('users.csv', 'a') as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])

# alt

# import csv
    
# def add_user(first_name, last_name):
#     with open("users.csv", "a") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         csv_writer.writerow([first_name, last_name])