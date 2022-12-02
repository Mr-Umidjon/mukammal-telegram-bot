import requests
import logging

url = "https://background-removal.p.rapidapi.com/remove"

headers = {
    "content-type": "application/x-www-form-urlencoded",
    "X-RapidAPI-Key": "93276afb99mshbb44a141285744dp15a659jsn2e7b918d0b31",
    "X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}


async def remove_background(img_url):
    payload = f"image_url={img_url}"
    response = requests.request("POST", url, data=payload, headers=headers)
    logging.info(response.json()['response']['image_url'])
    return response.json()['response']['image_url']
