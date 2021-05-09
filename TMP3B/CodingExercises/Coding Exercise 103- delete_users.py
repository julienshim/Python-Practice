'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

from csv import reader, writer

def delete_users(first, last):
    removed = 0

    with open("users.csv") as csvfile:
        csv_reader = reader(csvfile)
        users = list(csv_reader)

    with open("users.csv", "w") as csvfile:
        csv_writer = writer(csvfile)
        for user in users:
            [f, l] = user
            if f == first and l == last:
                removed += 1
            else:
                csv_writer.writerow(user)

    return "Users deleted: {}.".format(removed)

# alt

# import csv
    
# def delete_users(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
    
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == first_name and row[1] == last_name:
#                 count += 1
#             else:
#                 csv_writer.writerow(row)
    
#     return "Users deleted: {}.".format(count)