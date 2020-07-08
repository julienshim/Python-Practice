import requests

# res = requests.get('https://news.ycombinator.com/')

# print(res)
# print(res.ok)
# print(res.headers)
# print(res.text)

url = "http://www.google.com"  # 200
# url = "http://www.google.com/cat/blog" #404
response = requests.get(url)
print(
    f'Your request to {url} came back with status code {response.status_code}')
