# Красим вывод
from colorama import Fore, Back, Style


# Создание заметки.
import create_note_function
# Обновление заметки.
from update_note_function import update_note
# Поиск заметки
from search_notes_function import search_notes
#Удаление заявки
from delete_note import delete_note
# Форматированный вывод списка
from display_notes_function import display_note

# Меню.
def menu_function (notes):
    tuple_menu = ("Вывести текущие заметки", "Добавить заметку", "Удалить заметку", "Изменить заметку", "Найти заметку", "Выход")
    check_menu = True
    print(Fore.LIGHTWHITE_EX + "Добро пожаловать в Менеджер заметок!")
    while check_menu:
        print("\n" + Back.RESET + Fore.LIGHTWHITE_EX + "Главное меню.")
        print("Выберите пункт из меню, вводом нужной цифры:")
        for i in range(len(tuple_menu)):
            print(f"[{i}]: {tuple_menu[i]}")
        input_menu = int(input())
        if input_menu == 0:
            if notes:
                full = True
                if input(
                        Fore.LIGHTCYAN_EX + "\n Если Вы хотите получить только ID, имя пользователя и заголовок заметки, введите Да:").capitalize() == "Да":
                    full = False
                print(Fore.LIGHTGREEN_EX + "Собранная информация о заметках:")
                display_note(notes,None ,full)
            else:
                print(Fore.LIGHTRED_EX + "Нет сохраненных заметок.")
        elif input_menu == 1:
            create_note_function.add_note(notes)
        elif input_menu == 2:
            delete_note(notes)
        elif input_menu == 3:
            if notes:
                print("\n" + Fore.LIGHTRED_EX + "Собранная информация о заметках:")
                display_note(notes)
                update_note(notes)
            else:
                print(Fore.LIGHTRED_EX + "Нет сохраненных заметок.")
        elif input_menu == 4:
            status = None
            key = None
            if input(Fore.LIGHTCYAN_EX + "Если Вы хотите сделать поиск по статусу, то введите Да:").capitalize() == "Да":
                status = create_note_function.get_status()
            if input(Fore.LIGHTCYAN_EX + "Если Вы хотите сделать поиск по ключевому слову, то введите Да:").capitalize() == "Да":
                key = create_note_function.get_input("Введите ключевое слово для поиска в ключах Имя, Заголовок, Описание, Статус:")
            search_notes(notes, key, status)
        elif input_menu == 5:
            print(Fore.LIGHTGREEN_EX +"Программа завершается, до свидания!")
            exit(0)

# Файл для хранения всех заметок. Предварительно заполнены 3 заметки, чтобы не вводить каждый раз.
notes = [{'ID': '1', 'Имя': 'Алексей', 'Заголовок': 'Список покупок', 'Описание': 'Купить продукты на неделю', 'Статус': 'Новая', 'Дата начала': create_note_function.create_date("2025-01-10"), 'Дата истечения': create_note_function.create_date("2025-01-17")},
         {'ID': '2', 'Имя': 'Мария', 'Заголовок': 'Учеба', 'Описание': 'Подготовиться к экзамену', 'Статус': 'В процессе', 'Дата начала': create_note_function.create_date("2025-01-08"), 'Дата истечения': create_note_function.create_date("2025-01-25")},
         {'ID': '3', 'Имя': 'Иван', 'Заголовок': 'План работы', 'Описание': 'Завершить проект', 'Статус': 'Выполнено', 'Дата начала': create_note_function.create_date("2025-01-01"), 'Дата истечения': create_note_function.create_date("2025-01-07")}]

menu_function(notes)