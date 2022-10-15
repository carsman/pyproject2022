import telebot
from telebot import types
bot = telebot.TeleBot('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Hello! This bot can help you to convert different units of measurement!')
    bot.send_message(m.chat.id, 'To convert something, please write /convert')
# Получение сообщений от юзера


# Команда start
@bot.message_handler(commands=["convert"])
def convert(m, res=False):
        # Добавляем две кнопки
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("🌡Temp")
        item2=types.KeyboardButton("⚖Weight")
        item3 = types.KeyboardButton("📐Lenght")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(m.chat.id, 'What type of data you want to convert?',  reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global qtype, question, newinch
    if message.text == "🌡Temp":
        bot.send_message(message.chat.id, "Write temperature do you want to convert")
        question = message.text
        qtype = "t"
    elif message.text == "⚖Weight":
        bot.send_message(message.chat.id, "Write weight do you want to convert")
        question = message.text
        qtype = "w"
    elif message.text == "📐Lenght":
        bot.send_message(message.chat.id, "Write lenght do you want to convert")
        question = message.text
        qtype = "l"
    else:
        if qtype == "t1":
            bot.send_message(message.chat.id, "temp is ...")
            type = ""
        elif qtype == "w1":
            bot.send_message(message.chat.id, "weight is ...")
            type = ""
        elif qtype == "l1":
            bot.send_message(message.chat.id, "lenght is ...")
            qtype = ""
        else:
            bot.send_message(message.chat.id, "To witch unit it should be transferred?")
            qtype += "1"
            newinch = message.text
# Запускаем бота
bot.polling(none_stop=True, interval=0)