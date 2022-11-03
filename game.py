import telebot
from telebot import types
bot = telebot.TeleBot("5693058882:AAFh8E8dLgZeqCmvcqQeaPPR_DSugFlcCqU")


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Хотите начать игру",reply_markup=markup)
    bot.register_next_step_handler (start , epiz1 )

def epiz1 (message):
    pass

def walk (message):
    pass

def sit (message):
    pass

def choise (message):
    pass

def door (message):
    pass

def shelf (message):
    pass

def bed (message):
    pass

def box (message):
    pass

def exit (message):
    pass

bot.infinity_polling()
