import requests
from pprint import pprint as print

url = 'https://v6.exchangerate-api.com/v6/acf0771ed2408b694bd146db/pair/USD/UZS'

response = requests.get(url)

data = response.json()

print(data)