import requests

ULR = "https://api.thecatapi.com/v1/images/search"

result = requests.get(ULR)

data = result.json()

print(data)
