import colorama
import sqlite3
from sqlite3 import IntegrityError

from utils import tuple_keys, check_exist_notes


def save_note_to_db(notes, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(f"CREATE TABLE IF NOT EXISTS notes ({tuple_keys[0]} INTEGER PRIMARY KEY,{tuple_keys[1]} TEXT NOT NULL,"
                   f"{tuple_keys[2]} TEXT NOT NULL,{tuple_keys[3]} TEXT NOT NULL,{tuple_keys[4]} TEXT NOT NULL,"
                   f"{tuple_keys[5]} TEXT NOT NULL,{tuple_keys[6]} TEXT NOT NULL);")
    try:
        cursor.executemany(f"INSERT INTO notes VALUES(:{tuple_keys[0]}, :{tuple_keys[1]}, :{tuple_keys[2]}, "
            f":{tuple_keys[3]}, :{tuple_keys[4]}, :{tuple_keys[5]}, :{tuple_keys[6]})", notes)
        connection.commit()
    except IntegrityError:
        print(colorama.Fore.LIGHTRED_EX + "В Базе данных уже существует строка с данным ID."
              " Данные не записаны.")
    connection.close()

def load_notes_from_db(notes, db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    temp_list = []
    for row in cursor.execute("SELECT * FROM notes ORDER BY id"):
        temp_list.append(dict(zip(tuple_keys, row)))
    connection.close()
    new_notes = check_exist_notes(notes, temp_list)
    if new_notes:
        notes.extend(new_notes)