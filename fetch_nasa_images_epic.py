import os
import requests
from tools import dowloand_image
from dotenv import load_dotenv
import datetime


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
        dowloand_image(image_url, filepath, params=payload)

if __name__ == '__main__':
    load_dotenv()
    api_key = os.getenv("NASA_API_KEY")
    os.makedirs("images", exist_ok=True)
    fetch_nasa_images_epic(api_key)