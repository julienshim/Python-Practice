'''
update_users("Grace", "Hopper", "Hello", "World") # Users updated: 1.
update_users("Colt", "Steele", "Boba", "Fett") # Users updated: 2.
update_users("Not", "Here", "Still not", "Here") # Users updated: 0.
'''

from csv import DictReader, DictWriter

def update_users(old_first, old_last, new_first, new_last):
    updates = 0

    with open('users.csv') as file:
        csv_reader = DictReader(file)
        users = list(csv_reader)
        
    with open ('users.csv', "w") as file:
        headers = ["First Name", "Last Name"]
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for user in users:
            if user["First Name"] == old_first and user["Last Name"] == old_last:
                csv_writer.writerow({
                    "First Name": new_first,
                    "Last Name" : new_last
                })
                updates += 1
            else:
                csv_writer.writerow(user)

    return "Users updated: {}.".format(updates)


# alt 

# import csv

# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)

#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == old_first and row[1] == old_last:
#                 csv_writer.writerow([new_first, new_last])
#                 count += 1
#             else:
#                 csv_writer.writerow(row)

#     return "Users updated: {}.".format(count)