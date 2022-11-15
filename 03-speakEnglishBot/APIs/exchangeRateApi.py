import requests
from pprint import pprint as print

API_KEY = 'acf0771ed2408b694bd146db'
currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
print(response)
print(response.status_code)

json_data = response.json()
print(json_data)

current_rate = json_data['conversion_rate']
print(f"Current rate: 1 dollar: {current_rate} sum")