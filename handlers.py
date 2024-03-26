from main import bot
from keyboards import start_keyboard


@bot.message_handler(commands=['start'])
def start_handler(message):
    global name
    name = message.from_user.first_name
    photo = open('pictures/menu.jpeg', 'rb')
    bot.send_photo(message.from_user.id, photo, caption=f"Привет, {name}!Добро пожаловать\
                   в мир незабываемых фуршетов, шоколадных, сырных фонтанов и других вкусностей!\
                   \n\nЧем могу помочьjhbjhb?", parse_mode='html', reply_markup=start_keyboard())


@bot.message_handler(commands=['link'])
def link_handler(message):
    bot.send_message(message.from_user.id, text="Наcfccш сайт\n\n https://chocomechta.ru/", parse_mode='html')


# Любое необработанное сообщение
@bot.message_handler()
def any_text(message):
    bot.send_message(message.from_user.id, f"Я пока не научился общаться с людьми\
 Пожалуйста, нажми на какую-либо кнопку")
