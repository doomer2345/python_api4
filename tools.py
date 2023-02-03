import requests
from urllib.parse import urlparse
from os.path import splitext


def dowloand_image(url, filepath, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(filepath, 'wb') as file:
        file.write(response.content)


def get_file_extension(url):
    file_path = urlparse(url).path
    return splitext(file_path)[1]
