import telebot
from consts import TOKEN
from main import bot
from keyboards import start_keyboard


bot = telebot.TeleBot(TOKEN)

if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)