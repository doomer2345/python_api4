import requests
import os
from urllib.parse import urlparse
from os.path import splitext
import datetime
from dotenv import load_dotenv


def dowloand_images(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_spacex_images():
    spacex_url = "https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384"
    response = requests.get(spacex_url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    for number, link in enumerate (links):
        filepath = os.path.join("images", f"spacex{number}.jpg")
        dowloand_images(link, filepath)


def fetch_nasa_images_apod(api_key):
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    count = 45
    payload = {"api_key": api_key, "count": count}
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filepath = os.path.join("images", f"nasa_apod{number}{file_extension(image['url'])}")
        dowloand_images(image["url"], filepath)


def fetch_nasa_images_epic(api_key):
    nasa_epic_url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {"api_key": api_key}
    response = requests.get(nasa_epic_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filepath = os.path.join("images", f"nasa_epic{number}.png")
        image_name = image["image"]
        date_image = image["date"]
        date_time = datetime.datetime.fromisoformat(date_image)
        date = date_time.strftime('%Y/%m/%d')
        image_url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{image_name}.png"
        dowloand_images(image_url, filepath, params=payload)


def file_extension(url):
    file_path = urlparse(url).path
    return splitext(file_path)[1]

if __name__ == '__main__':
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    fetch_spacex_images()
    api_key=os.getenv("API_KEY")
    fetch_nasa_images_apod(api_key)
    fetch_nasa_images_epic(api_key)