import logging
import os
import requests

from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()


bot = TeleBot(token=f'{os.getenv('TOKEN')}')


logging.basicConfig(
    filename='kittybot.log',
    encoding='utf-8',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s, %(lineno)d',
    level=logging.INFO,
)


URL = 'https://api.thecatapi.com/v1/images/search'
NEW_URL = 'https://api.thedogapi.com/v1/images/search'


def get_new_image():
    try:
        response = requests.get(URL)
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        response = requests.get(NEW_URL)

    return response.json()[0].get('url')


@bot.message_handler(commands=['start'])
def wake_up(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton('/newcat'))

    bot.send_message(
        chat_id=message.chat.id,
        text=f'Привет, {message.chat.first_name}. '
        'Посмотри, какого котика я тебе нашёл',
        reply_markup=keyboard
    )
    bot.send_photo(
        chat_id=message.chat.id,
        photo=get_new_image()
    )


@bot.message_handler(commands=['newcat'])
def new_cat(message):
    bot.send_photo(
        chat_id=message.chat.id,
        photo=get_new_image()
    )


@bot.message_handler(content_types=['text'])
def say_hi(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Привет, я KittyBot!'
    )


def main():
    bot.polling()


if __name__ == '__main__':
    main()
