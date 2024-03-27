import telebot
from consts import TOKEN
from keyboards import start_keyboard


bot = telebot.TeleBot(TOKEN)
from callbacks import *
from handlers import *

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)