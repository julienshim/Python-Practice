more_numbers = [6, 1, 8, 2]
# sorted works on anything iterable
print(sorted(more_numbers))  # [1, 2, 6, 8]
print(sorted(more_numbers, reverse=True))  # [8, 6, 2, 1]
print(more_numbers)  # [6, 1, 8, 2]
print(sorted((2, 1, 45, 23, 99)))  # returns list [1, 2, 23, 45, 99]

users = [
    {"username": "samuel", "tweets": ['I love cake', 'I love pie']},
    {"username": "kate", "tweets": ['I love cake', 'I love my cat']},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ['dogs are the best', 'I\'m hungry']},
    {"username": "guitar_gal", "tweets": []}
]

# print(sorted(users, key=len))
# print(sorted(users, key=lambda user: user['username']))
# print(sorted(users, key=lambda user: len(user['tweets']), reverse=True))

songs = [
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

print(sorted(songs, key=lambda s: s['playcount'], reverse=True))
