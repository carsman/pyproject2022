import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hey, bitch!")

async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_caps = ' '.join(context.args) + " is equal to " + "tut budet otvet"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)
if __name__ == '__main__':
    application = ApplicationBuilder().token('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA').build()
    convert_handler = CommandHandler('convert', convert)
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    application.add_handler(convert_handler)
    application.run_polling()