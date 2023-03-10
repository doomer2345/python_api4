import os
import requests
from tools import get_file_extension, dowloand_image
from dotenv import load_dotenv


def fetch_nasa_images_apod(api_key):
    nasa_apod_url = "https://api.nasa.gov/planetary/apod"
    images_amount = 45
    payload = {"api_key": api_key, "count": images_amount}
    response = requests.get(nasa_apod_url, params=payload)
    response.raise_for_status()
    for number, image in enumerate(response.json()):
        filepath = os.path.join("images", f"nasa_apod{number}{get_file_extension(image['url'])}")
        dowloand_image(image["url"], filepath)


if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    os.makedirs("images", exist_ok=True)
    fetch_nasa_images_apod(api_key)