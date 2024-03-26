from telebot import types

# Стартовая клавиатура
def start_keyboard():
    #InlineKeyboard
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Посмотреть меню", callback_data="menu")
    markup.row(btn1)
    # btn2 = types.KeyboardButton("Узнать прайс-лист")
    btn3 = types.InlineKeyboardButton(text="Сделать заказ", callback_data="order")
    markup.row(btn3)
    # btn4 = types.KeyboardButton("Перейти на сайт")
    btn5 = types.InlineKeyboardButton(text="Связаться с менеджером", callback_data="manager")
    markup.row(btn5)

    return markup

from buttons import back_button

# Меню клавиатура
def menu_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Шоколадные фонтаны", callback_data='chocolate')
    btn2 = types.InlineKeyboardButton("Сырные фонтаны", callback_data='cheese')
    btn3 = types.InlineKeyboardButton("Фуршеты", callback_data='buffets')

    keyboard.row(btn1)
    keyboard.row(btn2)
    keyboard.row(btn3)
    keyboard.row(back_button())

    return keyboard


