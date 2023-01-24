import os
import requests
from main import dowloand_images, file_extension
from dotenv import load_dotenv


def dowloand_images(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def fetch_nasa_images_apod(api_key):
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    count = 45
    payload = {"api_key": api_key, "count": count}
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filepath = os.path.join("images", f"nasa_apod{number}{file_extension(image['url'])}")
        dowloand_images(image["url"], filepath)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("API_KEY")
    os.makedirs("images", exist_ok=True)
    fetch_nasa_images_apod(api_key)