import telegram


bot = telegram.Bot(token = "5942208451:AAE7EZv249efjuC6x4kmhOLdtoAA5MZ-ZgM")
bot.send_message(chat_id="@supephoto", text="Здравстсвуйте")
file_path = "images/nasa_apod4.jpg"
with open(file_path, 'rb') as photo:
    bot.send_photo(chat_id="@supephoto", photo=photo)
