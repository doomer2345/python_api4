### Описание проекта

Скрипт позволяет скачивать изображения с помощью сайтов SpaceX и NASA, а также отпрпавлять отправлять данные изображение с помощью телеграмм бота

### Как установить

Телеграмм токен вы можете получить у телеграмм бота BotFather. После того как получилось достать токен нужно создать файл .env и положить туда все данные:
```
CHAT_ID=id вашего чата
TELEG_TOKEN=телеграмм токен
API_KEY=ключ nasa
POST_TIME=время через которое будет отправляться ваша картинка
SPACEX_LAUNCH_ID=id запуска spacex
```

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Как запустить скрипт

Для запуска скрипта для скачивания фоток nasa пишите команду:
```
python fetch_nasa_images_epic.py

python fetch_nasa_images_apod.py
```
для фоток spacex пишите команду:
```
python fetch_spacex_images.py
```
для запуска бота используйте команду:
```
python telegram_bot.py
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).