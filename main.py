from functions import *
INPUT = 1
if __name__ == '__main__':
    application = ApplicationBuilder().token('5403325384:AAHEje2j4h1ERaK5Dk5yry5BGBzT_lY59zA').build()
    convert_handler = CommandHandler('convert', convert)
    start_handler = CommandHandler('start', start)
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(start_handler)
    application.add_handler(convert_handler)
    application.add_handler(CallbackQueryHandler(button))
    application.run_polling()


    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("convert", convert)],
        states={
            INPUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, convert)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    application.add_handler(conv_handler)