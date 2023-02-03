import os
import requests
from tools import dowloand_image


def fetch_spacex_image():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate (links):
        filepath = os.path.join("images", f"spacex{number}.jpg")
        dowloand_image(link, filepath)

if __name__ == '__main__':
    os.makedirs("images", exist_ok=True)
    fetch_spacex_image()