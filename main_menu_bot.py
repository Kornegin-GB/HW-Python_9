import db
from telegram import (
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove
)
from telegram.ext import (
    ConversationHandler,
)

start_keyboard = [
    ['/start_create - Обработать запись', '/read - Прочитать справочник'],
    ['/clear - Очистить справочник', '/exit - Завершить работу']
]
start_markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=False)


def start(update, context):
    update.message.reply_text(
        "Здравствуйте.\nЯ БОТ телефонный справочник\nЧтобы начать выберите пункт меню", reply_markup=start_markup
    )


def read(update, context):
    update.message.reply_text("Записи которые я нашел")
    for item in db.read_db():
        lst = " | ".join([str(i) for i in item])
        update.message.reply_text(lst)


def clear(update, context):
    update.message.reply_text("Справочник очищен")
    db.delete_db()


def stop(update, context):
    update.message.reply_text(
        "Я прощаюсь с вами. До свидание\nЧтобы возобновить работу введите /start", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END
