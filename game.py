import telebot
from telebot import types
bot = telebot.TeleBot("5693058882:AAFh8E8dLgZeqCmvcqQeaPPR_DSugFlcCqU")


@bot.message_handler(commands=['start', 'help'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Хотите начать игру",
                     reply_markup=markup)


bot.infinity_polling()
