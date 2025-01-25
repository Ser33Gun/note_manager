# Красим вывод
from colorama import Fore, Back

# Создание, обновление, поиск, удаление заметки.
from utils import add_note, update_note, check_exist_notes, search_notes, delete_note, display_searching_notes

#Чтение / Запись в файл
from data import save_notes_json, load_notes_json, save_note_to_db, load_notes_from_db

# Форматированный вывод списка
from interface import display_note

# Меню.
def menu_function (notes):
    tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку",
                  "Найти заметку", "Прочитать из файла","Записать в файл", "Добавить в БД", "Считать с БД" , "Выход")
    print(Fore.LIGHTWHITE_EX + "Добро пожаловать в Менеджер заметок!")
    # Меню отображается в бесконечном цикле, выход по ключу меню.
    while True:
        print("\n" + Back.RESET + Fore.LIGHTWHITE_EX + "Главное меню.")
        print("Выберите пункт из меню, вводом нужной цифры:")
        for i in range(len(tuple_menu)):
            print(f"[{i}]: {tuple_menu[i]}")
        try:
            input_menu = int(input())
        except ValueError:
            print(Fore.LIGHTRED_EX + "Введен некорректный ключ. Повторите ввод!")
            continue
        if input_menu == 0:
            display_note(notes,None)
        elif input_menu == 1:
            add_note(notes)
        elif input_menu == 2:
            delete_note(notes)
        elif input_menu == 3:
            display_note(notes)
            if notes:
                update_note(notes)
        elif input_menu == 4:
            display_searching_notes(search_notes(notes))
        elif input_menu == 5:
            rf = check_exist_notes(notes, load_notes_json('../ex.json'))
            if rf:
                notes.extend(rf)
                print(Fore.LIGHTGREEN_EX + "Добавление значений из файла произведена успешно!")
        elif input_menu == 6:
            save_notes_json(notes, '../ex.json')
        elif input_menu == 7:
            save_note_to_db(notes, '../data/notes.db')
        elif input_menu == 8:
            load_notes_from_db(notes, '../data/notes.db')
        elif input_menu == 9:
            print(Fore.LIGHTGREEN_EX + "Программа завершается, до свидания!")
            break
        else:
            print(Fore.LIGHTRED_EX + "Введен ключ, отсутствующий в списке. Повторите ввод!")

# Файл для хранения всех заметок.
notes = []

if __name__ == '__main__':
    menu_function(notes)