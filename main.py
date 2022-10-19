import re
import telebot
import wikipedia
from telebot import types

from convert import *

bot = telebot.TeleBot('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA')


@bot.message_handler(commands=["wiki"])
def wiki(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Millimetre"))
    markup.add(types.KeyboardButton("Centimetre"))
    markup.add(types.KeyboardButton("Decimetre"))
    markup.add(types.KeyboardButton("Metre"))
    markup.add(types.KeyboardButton("Kilometre"))
    markup.add(types.KeyboardButton("Mile"))
    markup.add(types.KeyboardButton("Foot"))
    markup.add(types.KeyboardButton("Inch"))
    markup.add(types.KeyboardButton("Yard"))
    markup.add(types.KeyboardButton("Gram"))
    markup.add(types.KeyboardButton("Kilogram"))
    markup.add(types.KeyboardButton("Ounce"))
    markup.add(types.KeyboardButton("Celsius"))
    markup.add(types.KeyboardButton("Kelvin"))
    markup.add(types.KeyboardButton("Fahrenheit"))
    bot.send_message(message.chat.id, 'What info do you want to get?', reply_markup=markup)
    bot.register_next_step_handler(message, wiki_choosing)


def wiki_choosing(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, getwiki(message.text), reply_markup=markup)
    bot.send_message(message.chat.id, 'Press /wiki to learn about other units or /convert to make a convert')


@bot.message_handler(commands=["convert"])
def convert(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🌡Temp")
    item2 = types.KeyboardButton("⚖Weight")
    item3 = types.KeyboardButton("📐length")
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    bot.send_message(message.chat.id, 'What type of data you want to convert?', reply_markup=markup)
    bot.register_next_step_handler(message, type_choosing)


def type_choosing(message):
    markup = types.ReplyKeyboardRemove(selective=False)
    if message.text == "🌡Temp":
        bot.send_message(message.chat.id, "Write temperature do you want to convert", reply_markup=markup)
        bot.register_next_step_handler(message, get_initial_temp)
    elif message.text == "⚖Weight":
        bot.send_message(message.chat.id, "Write weight do you want to convert", reply_markup=markup)
        bot.register_next_step_handler(message, get_initial_weight)

    elif message.text == "📐length":
        bot.send_message(message.chat.id, "Write length do you want to convert", reply_markup=markup)
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
    bot.send_message(message.chat.id, "Answer: " + str(temperature(n, var1.lower(), newinch.lower())) + newinch)
    bot.send_message(message.chat.id, 'Press /wiki to learn about units or /convert to make a new convert')


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
    bot.send_message(message.chat.id, "Answer: " + str(weight(n, var1.lower(), newinch.lower())) + newinch)
    bot.send_message(message.chat.id, 'Press /wiki to learn about units or /convert to make a new convert')


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
    bot.send_message(message.chat.id, "Answer: " + str(length(n, var1.lower(), newinch.lower())) + newinch)
    bot.send_message(message.chat.id, 'Press /wiki to learn about units or /convert to make a new convert')


def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'There is no such information in wikipedia'


@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Hello! This bot can help you to convert different units of measurement!')
    bot.send_message(m.chat.id, 'To convert something, please write /convert')


bot.polling(none_stop=True, interval=0)
