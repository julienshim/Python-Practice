print(max(3, 67, 99))  # 99
print(max('c', 'd', 'a'))  # d

nums = [40, 32, 6, 5, 10]
print(max(nums))  # 40
print(min(nums))  # 5

print(max('hello world'))  # w
print(min('hello world'))  # <space>

print(max((3, 5, 23, 65)))  # 65

names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

min(names)  # 'Arya'
max(names)  # 'Tim'

print(min(len(name) for name in names))  # 3
print(max(names, key=lambda n: len(n)))  # Ollivander
print(min(names, key=lambda n: len(n)))  # Tim

songs = [
    {"title": "Happy Birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# {'title': 'Happy Birthday', 'playcount': 1}
print(min(songs, key=lambda s: s['playcount']))
# {'title': 'YMCA', 'playcount': 99}
print(max(songs, key=lambda s: s['playcount']))
# 'YMCA'
print(max(songs, key=lambda s: s['playcount'])['title'])
