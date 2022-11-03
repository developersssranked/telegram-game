import telebot
from telebot import types
bot = telebot.TeleBot("5693058882:AAFh8E8dLgZeqCmvcqQeaPPR_DSugFlcCqU")

inventory = []


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton("Начать")
    markup.add(btn1)
    bot.send_message(message.chat.id, "Хотите начать игру",
                     reply_markup=markup)
    bot.register_next_step_handler(start, epiz1)


def epiz1(message):
    pass


def walk(message):
    pass


def sit(message):
    pass


def choise(message):
    if "Кровать" == message.text:
        mess = bot.send_message(message.chat.id, "Вы идете к кровати")
        bot.register_next_step_handler(mess, bed)
    elif "Дверь" == message.text:
        mess = bot.send_message(message.chat.id, "Вы идете к двери")
        bot.register_next_step_handler(mess, door)
    elif "Тумбочка" == message.text:
        mess = bot.send_message(message.chat.id, "Вы идете к тумбочке")
        bot.register_next_step_handler(mess, box)
    elif "Шкаф" == message.text:
        mess = bot.send_message(message.chat.id, "Вы идете к Шкафу")
        bot.register_next_step_handler(mess, shelf)


def door(message):
    if "Ключ" in inventory:
        bot.send_message(message.chat.id, "Вы успешно выбрались из комнаты")
    else:
        mess = bot.send_message(
            message.chat.id, "Осмотрев дверь вы понимаете, что она закрыта на ключ")
        bot.register_next_step_handler(mess, walk)


def shelf(message):
    inventory.append("Молоток")
    mess = bot.send_message(
        message.chat.id, "Осмотрев шкаф вы находите там кучу одежды и молоток. Вы забираете молоток")
    bot.register_next_step_handler(mess, walk)


def bed(message):
    pass


def box(message):
    if "Молоток" in inventory:
        inventory.append("Ключ")
        mess = bot.send_message(
            message.chat.id, "Вы открываете тумбочку и находите там ключ")
        bot.register_next_step_handler(mess, walk)
    else:
        mess = bot.send_message(
            message.chat.id, "Тумбочка оказывается закрытой, нужно ее чем то выломать")
        bot.register_next_step_handler(mess, walk)


def exit(message):
    pass


bot.infinity_polling()
