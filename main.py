import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, CallbackQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! This bot can help you to convert different units of measurement!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="To convert something, please write /convert")

async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Temp", callback_data="1"),
            InlineKeyboardButton("Weight", callback_data="2"),
        ],
        [InlineKeyboardButton("Lenght", callback_data="3")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("What type of data you want to convert?", reply_markup=reply_markup)
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    await query.answer()

    await query.edit_message_text(text=f"Selected option: {query.data}")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Displays info on how to use the bot."""
    await update.message.reply_text("Use /start to test this bot.")
if __name__ == '__main__':
    application = ApplicationBuilder().token('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA').build()
    convert_handler = CommandHandler('convert', convert)
    start_handler = CommandHandler('start', start)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(start_handler)
    application.add_handler(convert_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()