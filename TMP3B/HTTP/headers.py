import requests

url = "https://icanhazdadjoke.com/"

options = {
    "Accept": "application/json"
}

response = requests.get(url, headers=options)
data = response.json()

print(data["joke"])
print(f'stats: {data["status"]}')
