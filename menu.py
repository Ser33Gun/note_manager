# Красим вывод
from colorama import Fore, Back, Style


# Создание заметки.
import create_note_function
#Запись в файл
from work_with_file import save_notes_json, load_notes_json
# Обновление заметки.
from update_note_function import update_note, check_exist_notes
# Поиск заметки
from search_notes_function import search_notes
#Удаление заявки
from delete_note import delete_note
# Форматированный вывод списка
from display_notes_function import display_note

# Меню.
def menu_function (notes):
    tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку", "Найти заметку", "Прочитать из файла","Записать в файл", "Выход")
    check_menu = True
    print(Fore.LIGHTWHITE_EX + "Добро пожаловать в Менеджер заметок!")
    while check_menu:
        print("\n" + Back.RESET + Fore.LIGHTWHITE_EX + "Главное меню.")
        print("Выберите пункт из меню, вводом нужной цифры:")
        for i in range(len(tuple_menu)):
            print(f"[{i}]: {tuple_menu[i]}")
        input_menu = int(input())
        if input_menu == 0:
            display_note(notes,None)
        elif input_menu == 1:
            create_note_function.add_note(notes)
        elif input_menu == 2:
            delete_note(notes)
        elif input_menu == 3:
            display_note(notes)
            if notes:
                update_note(notes)
        elif input_menu == 4:
            search_notes(notes)
        elif input_menu == 5:
            rf = check_exist_notes(notes, load_notes_json('ex1.json'))
            if rf:
                notes.extend(rf)
                print(Fore.LIGHTGREEN_EX + "Добавление значений из файла произведена успешно!")
        elif input_menu == 6:
            save_notes_json(notes, 'ex.json')
        elif input_menu == 7:
            print(Fore.LIGHTGREEN_EX +"Программа завершается, до свидания!")
            exit(0)

# Файл для хранения всех заметок.
notes = []
menu_function(notes)