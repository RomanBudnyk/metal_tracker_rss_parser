from time import sleep

import telebot

from parser_bot.constants import HOUR_IN_MS
from parser_bot.rss_parser import parse_rss

bot = telebot.TeleBot('')


@bot.message_handler(content_types=('text',))
def send_message(message):
    if message.text == '/start':
        while True:
            last_albums = parse_rss()
            send_to_user = '\n'.join(last_albums) if last_albums else 'No new albums :('
            bot.send_message(message.from_user.id, send_to_user)
            sleep(HOUR_IN_MS)
