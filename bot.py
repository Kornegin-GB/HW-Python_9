from token_bot import TOKEN
import main_menu_bot as mainbot
import create_menu_bot as createbot
from telegram.ext import (
    CommandHandler,
    Updater,
    ConversationHandler,
    MessageHandler,
    Filters
)


def main_bot():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    create_handler = ConversationHandler(
        entry_points=[CommandHandler("create_one", createbot.create_one)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, createbot.get_record_surname)],
            2: [MessageHandler(Filters.text & ~Filters.command, createbot.get_record_phone)],
            3: [MessageHandler(Filters.text & ~Filters.command, createbot.get_db)]
        },
        fallbacks=[CommandHandler("stop", mainbot.stop)]
    )

    delete_handler = ConversationHandler(
        entry_points=[CommandHandler("delete_one", createbot.delete_one)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, createbot.get_del_one_entry)]
        },
        fallbacks=[CommandHandler('stop', mainbot.stop)]
    )

    update_handler = ConversationHandler(
        entry_points=[CommandHandler("edit_one", createbot.edit_one)],
        states={
            0: [MessageHandler(Filters.text & ~Filters.command, createbot.create_one)],
            1: [MessageHandler(Filters.text & ~Filters.command, createbot.get_record_surname)],
            2: [MessageHandler(Filters.text & ~Filters.command, createbot.get_record_phone)],
            3: [MessageHandler(Filters.text & ~Filters.command, createbot.udate_db)]
        },
        fallbacks=[CommandHandler("stop", mainbot.stop)]
    )

    dp.add_handler(CommandHandler("start", mainbot.start))
    dp.add_handler(CommandHandler("read", mainbot.read))
    dp.add_handler(CommandHandler("clear", mainbot.clear))
    dp.add_handler(CommandHandler("back", mainbot.start))
    dp.add_handler(CommandHandler("exit", mainbot.stop))
    dp.add_handler(CommandHandler("start_create", createbot.start_create))
    dp.add_handler(create_handler)
    dp.add_handler(delete_handler)
    dp.add_handler(update_handler)

    updater.start_polling()
    updater.idle()
