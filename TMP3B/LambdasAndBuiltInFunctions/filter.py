nums = [1, 2, 3, 4]

evens = list(filter(lambda x: x % 2 == 0, nums))

# print(evens)

names = ["austin", "penny", "anthony", "angels", "billy"]

# print(names)

a_names = filter(lambda n: n[0] == 'a', names)

# print(list(a_names))

users = [
    {"username": "samuel", "tweets": ['I love cake', 'I love pie']},
    {"username": "kate", "tweets": ['I love cake', 'I love my cat']},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ['dogs are the best', 'I\'m hungry']},
    {"username": "guitar_gal", "tweets": []}
]

# inactive_users = filter(lambda x: len(x['tweets']) == 0, users)
# inactive_users = filter(lambda x: not x['tweets'], users)

# print(list(inactive_users))

inactive_usernames_upper = list(map(lambda user: user['username'].upper(),
                                    filter(lambda u: not u['tweets'], users)))

print(inactive_usernames_upper)

names = ['Lassie', 'Colt', 'Rusty']
instructor = list(map(lambda name: f'Your instructor is {name}',
                      filter(lambda value: len(value) < 5, names)))

# print(instructor)

# list comprehension versions (preferred)
print([f'Your instructor is {name}' for name in names if len(name) < 5])
print([user for user in users if not user['tweets']])
print([user['username'].upper() for user in users if not user['tweets']])
