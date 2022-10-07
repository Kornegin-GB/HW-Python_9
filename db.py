import sqlite3 as sql

TABLE_NAME = "phone_dict"

connect = sql.connect("db_phone.db", check_same_thread=False)
cursor = connect.cursor()
cursor.execute(f""" CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
    id      INTEGER      PRIMARY KEY AUTOINCREMENT,
    name    STRING (50),
    surname STRING (50),
    phone    STRING (100)
)
""")


def insert_db(data):  # Добавление нескольких записей
    try:
        query = f"INSERT INTO {TABLE_NAME} (name, surname, phone) VALUES(?, ?, ?);"
        if isinstance(data[0], tuple):
            cursor.executemany(query, data)
        else:
            cursor.execute(query, data)
    except sql.ProgrammingError:
        print("Не верный формат данных")
    connect.commit()


def delete_insert_db(data):  # Добавление нескольких записей
    cursor.executescript(
        f""" DELETE FROM {TABLE_NAME};
        UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{TABLE_NAME}';
        """
    )
    query = f"INSERT INTO {TABLE_NAME} (name, surname, phone) VALUES(?, ?, ?);"
    cursor.executemany(query, data)
    connect.commit()


def update_one_entry_db(data, num):  # Заменить одну запись
    update_query = f""" UPDATE {TABLE_NAME} set name = ?, surname = ?, phone = ? WHERE id = ? """
    data_query = [data[0], data[1], data[2], num]
    cursor.execute(update_query, data_query)
    connect.commit()


def delete_db():  # Очистить таблицу полностью
    cursor.execute(f""" DELETE FROM {TABLE_NAME} """)
    cursor.execute(
        f""" UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{TABLE_NAME}' """)
    connect.commit()


def delete_one_entry(num):  # Удалить одну запись таблицы
    delete_query = f""" DELETE FROM {TABLE_NAME} WHERE id = {num} """
    cursor.execute(delete_query)
    cursor.execute(f"SELECT * FROM {TABLE_NAME};")
    three_results = cursor.fetchall()
    lst_new = []
    for item in three_results:
        lst = list(item)
        del lst[0]
        item = tuple(lst)
        lst_new.append(item)
    delete_db()
    insert_db(lst_new)
    connect.commit()


def read_db():
    cursor.execute(f"SELECT * FROM {TABLE_NAME};")
    data = cursor.fetchall()
    connect.commit()
    return data
