import os
import requests
from main import dowloand_images


def fetch_spacex_images():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate (links):
        filepath = os.path.join("images", f"spacex{number}.jpg")
        dowloand_images(link, filepath)

if __name__ == '__main__':
    os.makedirs("images", exist_ok=True)
    fetch_spacex_images()