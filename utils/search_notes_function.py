from colorama import Fore

from interface import display_note
from utils import get_input, get_status, tuple_keys

# Мини функция возвращает bool, если найдено совпадение.
def search_logic (notes, i, j, keyword=None, status=None):
    if keyword is not None and status is not None:
        return keyword.lower() in notes[i][tuple_keys[j]].lower() and status.lower() == notes[i][tuple_keys[4]].lower()
    elif status is not None:
        return status.lower() == notes[i][tuple_keys[4]].lower()
    elif keyword is not None:
        return keyword.lower() in notes[i][tuple_keys[j]].lower()

# Непосредственно функция поиска.
def search_notes(notes):
    if not notes:
        print(Fore.LIGHTRED_EX + "Нет сохраненных заметок.")
        return

    keyword = status = None
    if input(Fore.LIGHTCYAN_EX + "Если Вы хотите сделать поиск по статусу, то введите Да:").capitalize() == "Да":
        status = get_status()
    if input(
            Fore.LIGHTCYAN_EX + "Если Вы хотите сделать поиск по ключевому слову, то введите Да:").capitalize() == "Да":
        keyword = get_input(
            "Введите ключевое слово для поиска в ключах Имя, Заголовок, Описание, Статус:")
    note = []
    if keyword is None and status is None:
        print(Fore.LIGHTRED_EX + "Ключевых слов не указано! Поиск не был произведен.")
        return
    for i in range(len(notes)):
        for j in range(1, len(tuple_keys)):
            if search_logic(notes, i, j, keyword, status):
                note.append(notes[i])
                break
    return note

def display_searching_notes(note):
    if note:
        display_note(note)
    else:
        print(Fore.LIGHTRED_EX + "Совпадений не найдено!")