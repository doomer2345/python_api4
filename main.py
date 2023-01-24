import requests
import os
from urllib.parse import urlparse
from os.path import splitext
from dotenv import load_dotenv


def dowloand_images(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def file_extension(url):
    file_path = urlparse(url).path
    return splitext(file_path)[1]


if __name__ == '__main__':
    os.makedirs("images", exist_ok=True)
    load_dotenv()
    api_key=os.getenv("API_KEY")
