from telebot import types

# Кнопка назад
def back_button():
    keyboard = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("Назад", callback_data='back')

    return button