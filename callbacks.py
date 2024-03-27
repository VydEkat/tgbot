from keyboards import start_keyboard, menu_keyboard
from main import bot
from handlers import name

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == "menu":
      bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
      bot.send_message(callback.message.chat.id, text="Наше меню:", reply_markup=menu_keyboard())
    elif callback.data == "back":
     bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
     photo = open('pictures/menu.jpeg', 'rb')
     bot.send_photo(callback.message.chat.id, photo, caption=f"<b>Привет, {name}!</b>\n\nДобро пожаловать\
 в мир незабываемых фуршетов, шоколадных, сырных фонтанов и других вкусностей!\
 Чем могу помочь?", parse_mode='html', reply_markup=start_keyboard())