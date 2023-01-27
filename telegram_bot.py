import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__ == '__main__':
    images = os.listdir("images")
    load_dotenv()
    tg_token = os.getenv("TELEG_TOKEN")
    bot = telegram.Bot(token=tg_token)
    while True:
        image = random.choice(images)
        images_path = os.path.join("images", image)
        with open(images_path, 'rb') as photo:
            bot.send_photo(chat_id="@supephoto", photo=photo)
        time.sleep(14400)


