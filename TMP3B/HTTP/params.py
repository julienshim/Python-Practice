import requests

url = "https://icanhazdadjoke.com/search"

header = {
    "Accept": "application/json"
}

param = {
    "term": "cat",
    "limit": 1
}

response = requests.get(url, headers=header, params=param)
data = response.json()

# print(data["joke"])
# print(f'stats: {data["status"]}')

print(data["results"])
