import telebot
from telebot import types

token = ''
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_func(message):
    bot.send_dice(message.chat.id)
    bot.send_message(message.chat.id, "I threw a dice")

@bot.message_handler(commands=["info"])
def info_func(message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="tg url", url="https://t.me/endlesszanxiety")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Creator's tg", reply_markup=keyboard)

@bot.message_handler(commands=["menu"])
def menu_func(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_start = types.KeyboardButton(text="Start")
    button_info = types.KeyboardButton(text="Info")
    keyboard.add(button_start, button_info)
    bot.send_message(message.chat.id, "Menu: ", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == "Start")
def handle_start_func(message):
    start_func(message)

@bot.message_handler(func=lambda message: message.text == "Info")
def handle_info_func(message):
    info_func(message)

if __name__ == '__main__':
    bot.infinity_polling()

