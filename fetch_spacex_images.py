import os
import requests
from tools import dowloand_image
from dotenv import load_dotenv


def fetch_spacex_image(spacex_iaunch_id):
    spacex_url = f"https://api.spacexdata.com/v5/launches/{spacex_iaunch_id}"
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate (links):
        filepath = os.path.join("images", f"spacex{number}.jpg")
        dowloand_image(link, filepath)

if __name__ == '__main__':
    load_dotenv()
    spacex_iaunch_id = os.getenv("SPACEX_LAUNCH_ID", "5eb87d42ffd86e000604b384")
    os.makedirs("images", exist_ok=True)
    fetch_spacex_image(spacex_iaunch_id)