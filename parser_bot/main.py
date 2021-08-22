from parser_bot.tele_bot import bot


if __name__ == '__main__':
    bot.polling(none_stop=True, long_polling_timeout=3600)
