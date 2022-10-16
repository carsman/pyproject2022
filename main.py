import telebot
from convert import *
from functions import *
from telebot import types
bot = telebot.TeleBot('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA')

@bot.message_handler(commands=["convert"])
def convert(message, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🌡Temp")
        item2 = types.KeyboardButton("⚖Weight")
        item3 = types.KeyboardButton("📐Lenght")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, 'What type of data you want to convert?',  reply_markup=markup)
        bot.register_next_step_handler(message, type_choosing)


def type_choosing(message):
    if message.text == "🌡Temp":
        bot.send_message(message.chat.id, "Write temperature do you want to convert")
        bot.register_next_step_handler(message, get_initial_temp)
    elif message.text == "⚖Weight":
        bot.send_message(message.chat.id, "Write weight do you want to convert")
        bot.register_next_step_handler(message, get_initial_weight)

    elif message.text == "📐length":
        bot.send_message(message.chat.id, "Write length do you want to convert")
        bot.register_next_step_handler(message, get_initial_length)


def get_initial_temp(message):
    global question
    question = message.text
    bot.send_message(message.chat.id, "To witch unit you want co convert?")
    bot.register_next_step_handler(message, get_temp)


def get_temp(message):
    global newinch, question
    newinch = message.text
    bot.send_message(message.chat.id, "Converting")
    n, var1 = question.split(" ")
    n = int(n)
    bot.send_message(message.chat.id, "Answer: " + str(temperature(n, var1, newinch)) + newinch)


def get_initial_weight(message):
    global question
    question = message.text
    bot.send_message(message.chat.id, "To witch unit you want co convert?")
    bot.register_next_step_handler(message, get_weight)


def get_weight(message):
    global newinch, question
    newinch = message.text
    bot.send_message(message.chat.id, "Converting")
    n, var1 = question.split(" ")
    n = int(n)
    bot.send_message(message.chat.id, "Answer: " + str(temperature2(n, var1, newinch)) + newinch)


def get_initial_length(message):
    global question
    question = message.text
    bot.send_message(message.chat.id, "To witch unit you want co convert?")
    bot.register_next_step_handler(message, get_length)


def get_length(message):
    global newinch, question
    newinch = message.text
    bot.send_message(message.chat.id, "Converting")
    n, var1 = question.split(" ")
    n = int(n)
    bot.send_message(message.chat.id, "Answer: " + str(temperature2(n, var1, newinch)) + newinch)


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Hello! This bot can help you to convert different units of measurement!')
    bot.send_message(m.chat.id, 'To convert something, please write /convert')



# Запускаем бота
bot.polling(none_stop=True, interval=0)