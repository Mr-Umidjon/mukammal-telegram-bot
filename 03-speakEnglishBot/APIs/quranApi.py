import requests
from pprint import pprint as print

sura = 1
oyat = 1
tafsir = "uzb-muhammadsodikmu"

url_oyat = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/5/10.json"
url_sura = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{tafsir}/5.json"
response = requests.get(url_oyat)
print(response.status_code)

json_data = response.json()
print(json_data)


response = requests.get(url_sura)
print(response.status_code)

json_data = response.json()
print(json_data)