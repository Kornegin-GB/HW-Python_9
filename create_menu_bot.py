import db
from telegram import (
    ReplyKeyboardMarkup,
)
from telegram.ext import (
    ConversationHandler,
)

create_keyboard = [
    ['/create_one - Создать запись', '/delete_one - Удалить запись'],
    ['/edit_one - Изменить запись', '/back - Назад']
]
create_markup = ReplyKeyboardMarkup(create_keyboard, one_time_keyboard=False)


def start_create(update, context):
    update.message.reply_text(
        "Что вы хотите сделать с записью?\nВыберите один из пунктов меню", reply_markup=create_markup)


def create_one(update, context):
    global num_update
    num_update = update.message.text
    global lst
    lst = []
    update.message.reply_text(
        "Введите Имя")
    return 1


def get_record_surname(update, context):
    global lst
    update.message.reply_text(
        "Введите Фамилию")
    lst.append(update.message.text)
    return 2


def get_record_phone(update, context):
    global lst
    update.message.reply_text(
        "Введите номер телефона")
    lst.append(update.message.text)
    return 3


def get_db(update, context):
    global lst
    update.message.reply_text(
        "Я записал данные\nМожете сообщить мне другую команду", reply_markup=create_markup)
    lst.append(update.message.text)
    db.insert_db(lst)
    return ConversationHandler.END


def delete_one(update, context):
    update.message.reply_text(
        "Введите номер записи для удаления")
    return 1


def get_del_one_entry(update, context):
    num = update.message.text
    update.message.reply_text(
        f"Запись id = {num} удалена", reply_markup=create_markup)
    db.delete_one_entry(int(num))
    return ConversationHandler.END


def edit_one(update, context):
    update.message.reply_text(
        "Введите номер записи для исправления")
    return 0


def udate_db(update, context):
    global lst
    global num_update
    update.message.reply_text(
        "Я исправил данные\nМожете сообщить мне другую команду", reply_markup=create_markup)
    lst.append(update.message.text)
    db.update_one_entry_db(lst, int(num_update))
    return ConversationHandler.END
