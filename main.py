import requests
url = "https://superheroapi.com/api/2619421814940190/search/name"
resp = requests.get(url)
print(resp)