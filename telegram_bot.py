import telegram
import os
import random
import time
from dotenv import load_dotenv


if __name__ == '__main__':
    images = os.listdir("images")
    load_dotenv()
    tg_token = os.getenv("TELEG_TOKEN")
    chat_id = os.getenv("TG_CHAT_ID")
    post_time = os.getenv("POST_TIME", "14400")
    bot = telegram.Bot(token=tg_token)
    while True:
        image = random.choice(images)
        images_path = os.path.join("images", image)
        with open(images_path, 'rb') as photo:
            bot.send_photo(chat_id=chat_id, photo=photo)
        time.sleep(int(post_time))


