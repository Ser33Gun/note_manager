from colorama import Fore, Style
from display_notes_function import display_note
from create_note_function import tuple_keys

# Мини функция возвращает bool, если найдено совпадение.
def search_logic (notes, i, j, keyword=None, status=None):
    if keyword is not None and status is not None:
        return keyword.lower() in notes[i][tuple_keys[j]].lower() and status.lower() == notes[i][tuple_keys[4]].lower()
    elif status is not None:
        return status.lower() == notes[i][tuple_keys[4]].lower()
    elif keyword is not None:
        return keyword.lower() in notes[i][tuple_keys[j]].lower()

#Непосредственно функция поиска.
def search_notes(notes, keyword=None, status=None):
    note = []
    if keyword is None and status is None:
        print(Fore.LIGHTRED_EX + "Ключевых слов не указано! Поиск не был произведен.")
        return
    for i in range(len(notes)):
        for j in range(1, len(tuple_keys) - 2): # Даты при поиске не учитываются.
            if search_logic(notes, i, j, keyword, status):
                note.append(notes[i])
                break
    if note:
        display_note(note)
    else:
        print(Fore.LIGHTRED_EX + "Совпадений не найдено!")