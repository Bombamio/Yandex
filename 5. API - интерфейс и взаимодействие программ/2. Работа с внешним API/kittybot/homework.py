import logging
import os
import requests

from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()


bot = TeleBot(token=f'{os.getenv('TOKEN')}')


logging.basicConfig(
    filename='homework.log',
    format='%(asctime)s, %(levelname)s, %(message)s',
    level=logging.INFO,
)


url = 'https://practicum.yandex.ru/api/user_api/homework_statuses/'
headers = {'Authorization': f'OAuth {os.getenv('HOMEWORK_TOKEN')}'}
payload = {'from_date': 0}

# homework_statuses = requests.get(url, headers=headers, params=payload)


def get_status():
    try:
        homework_statuses = requests.get(
            url, headers=headers, params=payload
        ).json()
    except Exception as error:
        logging.error(f'Ошибка при запросе к основному API: {error}')
        homework_statuses = None
    return homework_statuses


@bot.message_handler(commands=['start'])
def wake_up(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(types.KeyboardButton('/status'))

    bot.send_message(
        chat_id=message.chat.id,
        text=f'{get_status()}'
    )
    logging.info(f'{get_status()}')


@bot.message_handler(commands=['status'])
def new_status(message):
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Статус на данный момент:{get_status()}'
    )
    logging.info(f'{get_status()}')


def main():
    bot.polling()


if __name__ == '__main__':
    main()
